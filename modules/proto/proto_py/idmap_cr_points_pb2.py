# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: idmap_cr_points.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15idmap_cr_points.proto\x12\x05idmap\"F\n\x0bRespRequest\x12\x17\n\x0fresp_request_id\x18\x01 \x01(\x04\x12\x1e\n\x07\x63r_info\x18\x02 \x03(\x0b\x32\r.idmap.CRInfo\"@\n\x06\x43RInfo\x12\x12\n\nsd_path_id\x18\x02 \x01(\x04\x12\"\n\tcr_points\x18\x03 \x03(\x0b\x32\x0f.idmap.CRPoints\"X\n\x08\x43RPoints\x12&\n\x0f\x63r_start_points\x18\x01 \x01(\x0b\x32\r.idmap.CRGnss\x12$\n\rcr_end_points\x18\x02 \x01(\x0b\x32\r.idmap.CRGnss\"(\n\x06\x43RGnss\x12\x0e\n\x06\x63r_lng\x18\x01 \x01(\x01\x12\x0e\n\x06\x63r_lat\x18\x02 \x01(\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'idmap_cr_points_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RESPREQUEST._serialized_start=32
  _RESPREQUEST._serialized_end=102
  _CRINFO._serialized_start=104
  _CRINFO._serialized_end=168
  _CRPOINTS._serialized_start=170
  _CRPOINTS._serialized_end=258
  _CRGNSS._serialized_start=260
  _CRGNSS._serialized_end=300
# @@protoc_insertion_point(module_scope)
