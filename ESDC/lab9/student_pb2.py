# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: student.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='student.proto',
  package='lab9',
  syntax='proto3',
  serialized_options=b'\n\006io.stdB\007StudentP\001\242\002\003HLW',
  serialized_pb=b'\n\rstudent.proto\x12\x04lab9\"\x1a\n\x07Request\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1b\n\x08Response\x12\x0f\n\x07message\x18\x01 \x01(\t2c\n\x06HTTTSV\x12(\n\x05login\x12\r.lab9.Request\x1a\x0e.lab9.Response\"\x00\x12/\n\x0cview_profile\x12\r.lab9.Request\x1a\x0e.lab9.Response\"\x00\x42\x19\n\x06io.stdB\x07StudentP\x01\xa2\x02\x03HLWb\x06proto3'
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='lab9.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='lab9.Request.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=23,
  serialized_end=49,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='lab9.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='lab9.Response.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=51,
  serialized_end=78,
)

DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'student_pb2'
  # @@protoc_insertion_point(class_scope:lab9.Request)
  })
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'student_pb2'
  # @@protoc_insertion_point(class_scope:lab9.Response)
  })
_sym_db.RegisterMessage(Response)


DESCRIPTOR._options = None

_HTTTSV = _descriptor.ServiceDescriptor(
  name='HTTTSV',
  full_name='lab9.HTTTSV',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=80,
  serialized_end=179,
  methods=[
  _descriptor.MethodDescriptor(
    name='login',
    full_name='lab9.HTTTSV.login',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='view_profile',
    full_name='lab9.HTTTSV.view_profile',
    index=1,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_HTTTSV)

DESCRIPTOR.services_by_name['HTTTSV'] = _HTTTSV

# @@protoc_insertion_point(module_scope)
