# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: helloworld.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='helloworld.proto',
  package='helloworld',
  syntax='proto3',
  serialized_options=b'\n\033io.grpc.examples.helloworldB\017HelloWorldProtoP\001\242\002\003HLW',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10helloworld.proto\x12\nhelloworld\".\n\x0cSubscription\x12\x0c\n\x04\x63ity\x18\x01 \x03(\t\x12\x10\n\x08\x63\x61tegory\x18\x02 \x03(\t\"\x1f\n\x0cNotification\x12\x0f\n\x07message\x18\x01 \x01(\t2R\n\x0bNotificator\x12\x43\n\tsubscribe\x12\x18.helloworld.Subscription\x1a\x18.helloworld.Notification\"\x00\x30\x01\x42\x36\n\x1bio.grpc.examples.helloworldB\x0fHelloWorldProtoP\x01\xa2\x02\x03HLWb\x06proto3'
)




_SUBSCRIPTION = _descriptor.Descriptor(
  name='Subscription',
  full_name='helloworld.Subscription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='city', full_name='helloworld.Subscription.city', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='category', full_name='helloworld.Subscription.category', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=78,
)


_NOTIFICATION = _descriptor.Descriptor(
  name='Notification',
  full_name='helloworld.Notification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='helloworld.Notification.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=111,
)

DESCRIPTOR.message_types_by_name['Subscription'] = _SUBSCRIPTION
DESCRIPTOR.message_types_by_name['Notification'] = _NOTIFICATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Subscription = _reflection.GeneratedProtocolMessageType('Subscription', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIPTION,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.Subscription)
  })
_sym_db.RegisterMessage(Subscription)

Notification = _reflection.GeneratedProtocolMessageType('Notification', (_message.Message,), {
  'DESCRIPTOR' : _NOTIFICATION,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.Notification)
  })
_sym_db.RegisterMessage(Notification)


DESCRIPTOR._options = None

_NOTIFICATOR = _descriptor.ServiceDescriptor(
  name='Notificator',
  full_name='helloworld.Notificator',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=113,
  serialized_end=195,
  methods=[
  _descriptor.MethodDescriptor(
    name='subscribe',
    full_name='helloworld.Notificator.subscribe',
    index=0,
    containing_service=None,
    input_type=_SUBSCRIPTION,
    output_type=_NOTIFICATION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_NOTIFICATOR)

DESCRIPTOR.services_by_name['Notificator'] = _NOTIFICATOR

# @@protoc_insertion_point(module_scope)
