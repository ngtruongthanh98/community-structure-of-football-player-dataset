# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exchange.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x65xchange.proto\"&\n\x16RecommendPlayerRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x81\x01\n\x17RecommendPlayerResponse\x12\x39\n\x07players\x18\x01 \x03(\x0b\x32(.RecommendPlayerResponse.RecommendPLayer\x1a+\n\x0fRecommendPLayer\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t2_\n\nPlayerInfo\x12Q\n\x1aGetRecommendedPlayerByName\x12\x17.RecommendPlayerRequest\x1a\x18.RecommendPlayerResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'exchange_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RECOMMENDPLAYERREQUEST._serialized_start=18
  _RECOMMENDPLAYERREQUEST._serialized_end=56
  _RECOMMENDPLAYERRESPONSE._serialized_start=59
  _RECOMMENDPLAYERRESPONSE._serialized_end=188
  _RECOMMENDPLAYERRESPONSE_RECOMMENDPLAYER._serialized_start=145
  _RECOMMENDPLAYERRESPONSE_RECOMMENDPLAYER._serialized_end=188
  _PLAYERINFO._serialized_start=190
  _PLAYERINFO._serialized_end=285
# @@protoc_insertion_point(module_scope)