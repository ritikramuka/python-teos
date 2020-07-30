# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: appointment.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="appointment.proto",
    package="teos",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x11\x61ppointment.proto\x12\x04teos"\x18\n\x07Locator\x12\r\n\x05value\x18\x01 \x01(\t"\x1a\n\tSignature\x12\r\n\x05value\x18\x01 \x01(\t"]\n\x0b\x41ppointment\x12\x1e\n\x07locator\x18\x01 \x01(\x0b\x32\r.teos.Locator\x12\x17\n\x0f\x65ncrypted_block\x18\x02 \x01(\t\x12\x15\n\rto_self_delay\x18\x03 \x01(\r"c\n\x15\x41\x64\x64\x41ppointmentRequest\x12&\n\x0b\x61ppointment\x18\x01 \x01(\x0b\x32\x11.teos.Appointment\x12"\n\tsignature\x18\x02 \x01(\x0b\x32\x0f.teos.Signature"\xa7\x01\n\x16\x41\x64\x64\x41ppointmentResponse\x12\x1e\n\x07locator\x18\x01 \x01(\x0b\x32\r.teos.Locator\x12\x13\n\x0bstart_block\x18\x02 \x01(\r\x12"\n\tsignature\x18\x03 \x01(\x0b\x32\x0f.teos.Signature\x12\x17\n\x0f\x61vailable_slots\x18\x04 \x01(\r\x12\x1b\n\x13subscription_expiry\x18\x05 \x01(\r"[\n\x15GetAppointmentRequest\x12\x1e\n\x07locator\x18\x01 \x01(\x0b\x32\r.teos.Locator\x12"\n\tsignature\x18\x02 \x01(\x0b\x32\x0f.teos.Signature"p\n\x16GetAppointmentResponse\x12\x1e\n\x07locator\x18\x01 \x01(\x0b\x32\r.teos.Locator\x12\x0e\n\x06status\x18\x02 \x01(\t\x12&\n\x0b\x61ppointment\x18\x03 \x01(\x0b\x32\x11.teos.Appointmentb\x06proto3',
)


_LOCATOR = _descriptor.Descriptor(
    name="Locator",
    full_name="teos.Locator",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="value",
            full_name="teos.Locator.value",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=27,
    serialized_end=51,
)


_SIGNATURE = _descriptor.Descriptor(
    name="Signature",
    full_name="teos.Signature",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="value",
            full_name="teos.Signature.value",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=53,
    serialized_end=79,
)


_APPOINTMENT = _descriptor.Descriptor(
    name="Appointment",
    full_name="teos.Appointment",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="locator",
            full_name="teos.Appointment.locator",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="encrypted_block",
            full_name="teos.Appointment.encrypted_block",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="to_self_delay",
            full_name="teos.Appointment.to_self_delay",
            index=2,
            number=3,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=81,
    serialized_end=174,
)


_ADDAPPOINTMENTREQUEST = _descriptor.Descriptor(
    name="AddAppointmentRequest",
    full_name="teos.AddAppointmentRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="appointment",
            full_name="teos.AddAppointmentRequest.appointment",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="signature",
            full_name="teos.AddAppointmentRequest.signature",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=176,
    serialized_end=275,
)


_ADDAPPOINTMENTRESPONSE = _descriptor.Descriptor(
    name="AddAppointmentResponse",
    full_name="teos.AddAppointmentResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="locator",
            full_name="teos.AddAppointmentResponse.locator",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="start_block",
            full_name="teos.AddAppointmentResponse.start_block",
            index=1,
            number=2,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="signature",
            full_name="teos.AddAppointmentResponse.signature",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="available_slots",
            full_name="teos.AddAppointmentResponse.available_slots",
            index=3,
            number=4,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="subscription_expiry",
            full_name="teos.AddAppointmentResponse.subscription_expiry",
            index=4,
            number=5,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=278,
    serialized_end=445,
)


_GETAPPOINTMENTREQUEST = _descriptor.Descriptor(
    name="GetAppointmentRequest",
    full_name="teos.GetAppointmentRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="locator",
            full_name="teos.GetAppointmentRequest.locator",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="signature",
            full_name="teos.GetAppointmentRequest.signature",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=447,
    serialized_end=538,
)


_GETAPPOINTMENTRESPONSE = _descriptor.Descriptor(
    name="GetAppointmentResponse",
    full_name="teos.GetAppointmentResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="locator",
            full_name="teos.GetAppointmentResponse.locator",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="status",
            full_name="teos.GetAppointmentResponse.status",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="appointment",
            full_name="teos.GetAppointmentResponse.appointment",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=540,
    serialized_end=652,
)

_APPOINTMENT.fields_by_name["locator"].message_type = _LOCATOR
_ADDAPPOINTMENTREQUEST.fields_by_name["appointment"].message_type = _APPOINTMENT
_ADDAPPOINTMENTREQUEST.fields_by_name["signature"].message_type = _SIGNATURE
_ADDAPPOINTMENTRESPONSE.fields_by_name["locator"].message_type = _LOCATOR
_ADDAPPOINTMENTRESPONSE.fields_by_name["signature"].message_type = _SIGNATURE
_GETAPPOINTMENTREQUEST.fields_by_name["locator"].message_type = _LOCATOR
_GETAPPOINTMENTREQUEST.fields_by_name["signature"].message_type = _SIGNATURE
_GETAPPOINTMENTRESPONSE.fields_by_name["locator"].message_type = _LOCATOR
_GETAPPOINTMENTRESPONSE.fields_by_name["appointment"].message_type = _APPOINTMENT
DESCRIPTOR.message_types_by_name["Locator"] = _LOCATOR
DESCRIPTOR.message_types_by_name["Signature"] = _SIGNATURE
DESCRIPTOR.message_types_by_name["Appointment"] = _APPOINTMENT
DESCRIPTOR.message_types_by_name["AddAppointmentRequest"] = _ADDAPPOINTMENTREQUEST
DESCRIPTOR.message_types_by_name["AddAppointmentResponse"] = _ADDAPPOINTMENTRESPONSE
DESCRIPTOR.message_types_by_name["GetAppointmentRequest"] = _GETAPPOINTMENTREQUEST
DESCRIPTOR.message_types_by_name["GetAppointmentResponse"] = _GETAPPOINTMENTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Locator = _reflection.GeneratedProtocolMessageType(
    "Locator",
    (_message.Message,),
    {
        "DESCRIPTOR": _LOCATOR,
        "__module__": "appointment_pb2"
        # @@protoc_insertion_point(class_scope:teos.Locator)
    },
)
_sym_db.RegisterMessage(Locator)

Signature = _reflection.GeneratedProtocolMessageType(
    "Signature",
    (_message.Message,),
    {
        "DESCRIPTOR": _SIGNATURE,
        "__module__": "appointment_pb2"
        # @@protoc_insertion_point(class_scope:teos.Signature)
    },
)
_sym_db.RegisterMessage(Signature)

Appointment = _reflection.GeneratedProtocolMessageType(
    "Appointment",
    (_message.Message,),
    {
        "DESCRIPTOR": _APPOINTMENT,
        "__module__": "appointment_pb2"
        # @@protoc_insertion_point(class_scope:teos.Appointment)
    },
)
_sym_db.RegisterMessage(Appointment)

AddAppointmentRequest = _reflection.GeneratedProtocolMessageType(
    "AddAppointmentRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _ADDAPPOINTMENTREQUEST,
        "__module__": "appointment_pb2"
        # @@protoc_insertion_point(class_scope:teos.AddAppointmentRequest)
    },
)
_sym_db.RegisterMessage(AddAppointmentRequest)

AddAppointmentResponse = _reflection.GeneratedProtocolMessageType(
    "AddAppointmentResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _ADDAPPOINTMENTRESPONSE,
        "__module__": "appointment_pb2"
        # @@protoc_insertion_point(class_scope:teos.AddAppointmentResponse)
    },
)
_sym_db.RegisterMessage(AddAppointmentResponse)

GetAppointmentRequest = _reflection.GeneratedProtocolMessageType(
    "GetAppointmentRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETAPPOINTMENTREQUEST,
        "__module__": "appointment_pb2"
        # @@protoc_insertion_point(class_scope:teos.GetAppointmentRequest)
    },
)
_sym_db.RegisterMessage(GetAppointmentRequest)

GetAppointmentResponse = _reflection.GeneratedProtocolMessageType(
    "GetAppointmentResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETAPPOINTMENTRESPONSE,
        "__module__": "appointment_pb2"
        # @@protoc_insertion_point(class_scope:teos.GetAppointmentResponse)
    },
)
_sym_db.RegisterMessage(GetAppointmentResponse)


# @@protoc_insertion_point(module_scope)
