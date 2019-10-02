from binascii import hexlify, unhexlify
from queue import Queue
from threading import Thread
from pisa import logging, bitcoin_cli
from pisa.responder import Responder
from pisa.utils.zmq_subscriber import ZMQHandler
from pisa.utils.auth_proxy import JSONRPCException
from hashlib import sha256
from uuid import uuid4
from pisa.conf import MAX_APPOINTMENTS, EXPIRY_DELTA


class Watcher:
    def __init__(self, max_appointments=MAX_APPOINTMENTS):
        self.appointments = dict()
        self.locator_uuid_map = dict()
        self.block_queue = None
        self.asleep = True
        self.max_appointments = max_appointments
        self.zmq_subscriber = None
        self.responder = Responder()

    def add_appointment(self, appointment):
        # Rationale:
        # The Watcher will analyze every received block looking for appointment matches. If there is no work
        # to do the watcher can go sleep (if appointments = {} then asleep = True) otherwise for every received block
        # the watcher will get the list of transactions and compare it with the list of appointments.
        # If the watcher is awake, every new appointment will just be added to the appointment list until
        # max_appointments is reached.

        if len(self.appointments) < self.max_appointments:
            # Appointments are identified by the locator: the sha256 of commitment txid (H(tx_id)).
            # Two different nodes may ask for appointments using the same commitment txid, what will result in a
            # collision in our appointments structure (and may be an attack surface). In order to avoid such collisions
            # we will identify every appointment with a uuid

            uuid = uuid4().hex
            self.appointments[uuid] = appointment

            if appointment.locator in self.locator_uuid_map:
                self.locator_uuid_map[appointment.locator].append(uuid)

            else:
                self.locator_uuid_map[appointment.locator] = [uuid]

            if self.asleep:
                self.asleep = False
                self.block_queue = Queue()
                zmq_thread = Thread(target=self.do_subscribe, args=[self.block_queue])
                watcher = Thread(target=self.do_watch)
                zmq_thread.start()
                watcher.start()

                logging.info("[Watcher] waking up!")

            appointment_added = True

            logging.info('[Watcher] new appointment accepted (locator = {})'.format(appointment.locator))

        else:
            appointment_added = False

            logging.info('[Watcher] maximum appointments reached, appointment rejected (locator = {})'.format(
                appointment.locator))

        return appointment_added

    def do_subscribe(self, block_queue):
        self.zmq_subscriber = ZMQHandler(parent='Watcher')
        self.zmq_subscriber.handle(block_queue)

    def do_watch(self):
        while len(self.appointments) > 0:
            block_hash = self.block_queue.get()

            try:
                block = bitcoin_cli.getblock(block_hash)
                txids = block.get('tx')

                logging.info("[Watcher] new block received {}".format(block_hash))
                logging.info("[Watcher] list of transactions: {}".format(txids))

                self.delete_expired_appointment(block)

                potential_locators = {sha256(unhexlify(txid)).hexdigest(): txid for txid in txids}

                # Check is any of the tx_ids in the received block is an actual match
                # Get the locators that are both in the map and in the potential locators dict.
                intersection = set(self.locator_uuid_map.keys()).intersection(potential_locators.keys())
                potential_matches = {locator: potential_locators[locator] for locator in intersection}

                if len(potential_matches) > 0:
                    logging.info("[Watcher] list of potential matches: {}".format(potential_matches))
                else:
                    logging.info("[Watcher] no potential matches found")

                matches = self.check_potential_matches(potential_matches)

                for locator, uuid, dispute_txid, justice_txid, justice_rawtx in matches:
                    logging.info("[Watcher] notifying responder about {} and deleting appointment {} (uuid: {})"
                                 .format(justice_txid, locator, uuid))

                    self.responder.add_response(uuid, dispute_txid, justice_txid, justice_rawtx,
                                                self.appointments[uuid].end_time)

                    # Delete the appointment
                    self.appointments.pop(uuid)

                    # If there was only one appointment that matches the locator we can delete the whole list
                    if len(self.locator_uuid_map[locator]) == 1:
                        # ToDo: #9-add-data-persistency
                        self.locator_uuid_map.pop(locator)
                    else:
                        # Otherwise we just delete the appointment that matches locator:appointment_pos
                        # ToDo: #9-add-data-persistency
                        self.locator_uuid_map[locator].remove(uuid)

            except JSONRPCException as e:
                logging.error("[Watcher] couldn't get block from bitcoind. Error code {}".format(e))

        # Go back to sleep if there are no more appointments
        self.asleep = True
        self.zmq_subscriber.terminate = True

        logging.error("[Watcher] no more pending appointments, going back to sleep")

    def delete_expired_appointment(self, block):
        to_delete = [uuid for uuid, appointment in self.appointments.items() if block["height"] > appointment.end_time
                     + EXPIRY_DELTA]

        for uuid in to_delete:
            # ToDo: #9-add-data-persistency
            locator = self.appointments[uuid].locator

            self.appointments.pop(uuid)

            if len(self.locator_uuid_map[locator]) == 1:
                self.locator_uuid_map.pop(locator)

            else:
                self.locator_uuid_map[locator].remove(uuid)

            logging.info("[Watcher] end time reached with no match! Deleting appointment {} (uuid: {})".format(locator,
                                                                                                               uuid))

    def check_potential_matches(self, potential_matches):
        matches = []

        for locator, dispute_txid in potential_matches.items():
            for uuid in self.locator_uuid_map[locator]:
                try:
                    # ToDo: #20-test-tx-decrypting-edge-cases
                    justice_rawtx = self.appointments[uuid].encrypted_blob.decrypt(unhexlify(dispute_txid))
                    justice_rawtx = hexlify(justice_rawtx).decode()
                    justice_txid = bitcoin_cli.decoderawtransaction(justice_rawtx).get('txid')
                    matches.append((locator, uuid, dispute_txid, justice_txid, justice_rawtx))

                    logging.info("[Watcher] match found for locator {} (uuid: {}): {}".format(locator, uuid,
                                                                                              justice_txid))
                except JSONRPCException as e:
                    # Tx decode failed returns error code -22, maybe we should be more strict here. Leaving it simple
                    # for the POC
                    logging.error("[Watcher] can't build transaction from decoded data. Error code {}".format(e))

        return matches
