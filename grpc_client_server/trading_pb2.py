# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: trading.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rtrading.proto\x12\x0ctrade_server\"i\n\rActionRequest\x12\x14\n\x0crequest_type\x18\x01 \x01(\t\x12\x13\n\x06symbol\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x15\n\x08quantity\x18\x03 \x01(\x05H\x01\x88\x01\x01\x42\t\n\x07_symbolB\x0b\n\t_quantity\" \n\x0b\x41\x63tionReply\x12\x11\n\treply_msg\x18\x01 \x01(\t2Z\n\x0fTradingFunction\x12G\n\x0bsendRequest\x12\x1b.trade_server.ActionRequest\x1a\x19.trade_server.ActionReply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'trading_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ACTIONREQUEST']._serialized_start=31
  _globals['_ACTIONREQUEST']._serialized_end=136
  _globals['_ACTIONREPLY']._serialized_start=138
  _globals['_ACTIONREPLY']._serialized_end=170
  _globals['_TRADINGFUNCTION']._serialized_start=172
  _globals['_TRADINGFUNCTION']._serialized_end=262
# @@protoc_insertion_point(module_scope)
