# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: person.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cperson.proto\"~\n\x07Persons\x12 \n\x07persons\x18\x01 \x03(\x0b\x32\x0f.Persons.Person\x1aQ\n\x06Person\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\x14\n\x0c\x63ompany_name\x18\x04 \x01(\t\"\x07\n\x05\x45mpty20\n\rPersonService\x12\x1f\n\x0bRetreaveAll\x12\x06.Empty\x1a\x08.Personsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'person_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_PERSONS']._serialized_start=16
  _globals['_PERSONS']._serialized_end=142
  _globals['_PERSONS_PERSON']._serialized_start=61
  _globals['_PERSONS_PERSON']._serialized_end=142
  _globals['_EMPTY']._serialized_start=144
  _globals['_EMPTY']._serialized_end=151
  _globals['_PERSONSERVICE']._serialized_start=153
  _globals['_PERSONSERVICE']._serialized_end=201
# @@protoc_insertion_point(module_scope)
