# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ems.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tems.proto\x12\x08\x45msProto\"c\n\x06\x42usEms\x12\x33\n\x0f\x65ms_motion_info\x18\x01 \x01(\x0b\x32\x1a.EmsProto.BusEmsMotionInfo\x12$\n\x07\x65ms_sts\x18\x02 \x01(\x0b\x32\x13.EmsProto.BusEmsSts\"\xa2\x03\n\x10\x42usEmsMotionInfo\x12\x18\n\x10\x65ms_engine_speed\x18\x01 \x01(\x01\x12\x1b\n\x13\x65ms_frictional_torq\x18\x02 \x01(\x01\x12%\n\x1d\x65ms_indicated_driver_req_torq\x18\x03 \x01(\x01\x12#\n\x1b\x65ms_indicated_real_eng_torq\x18\x04 \x01(\x01\x12\x1e\n\x16\x65ms_max_indicated_torq\x18\x05 \x01(\x01\x12\x1e\n\x16\x65ms_min_indicated_torq\x18\x06 \x01(\x01\x12\x1b\n\x13\x65ms_torque_constant\x18\x07 \x01(\r\x12\x12\n\ntime_stamp\x18\x08 \x01(\x01\x12\x15\n\rmessage_valid\x18\t \x01(\r\x12\x11\n\treserved0\x18\n \x01(\r\x12\x11\n\treserved1\x18\x0b \x01(\r\x12\x11\n\treserved2\x18\x0c \x01(\r\x12\x11\n\treserved3\x18\r \x01(\r\x12\x11\n\treserved4\x18\x0e \x01(\r\x12\x11\n\treserved5\x18\x0f \x01(\r\x12\x11\n\treserved6\x18\x10 \x01(\r\"\xb5\x03\n\tBusEmsSts\x12\x1a\n\x12\x65ms_accpedel_error\x18\x01 \x01(\r\x12\x1c\n\x14\x65ms_acc_req_possible\x18\x02 \x01(\r\x12\x15\n\rems_acc_pedal\x18\x03 \x01(\x01\x12&\n\x1e\x65ms_apa_torq_request_available\x18\x04 \x01(\r\x12\x15\n\rems_ecgp_ovrd\x18\x05 \x01(\r\x12\x1e\n\x16\x65ms_engine_speed_error\x18\x06 \x01(\r\x12\x19\n\x11\x65ms_engine_status\x18\x07 \x01(\r\x12\"\n\x1a\x65ms_engine_status_with_stt\x18\x08 \x01(\r\x12\x12\n\nems_qecacc\x18\t \x01(\r\x12\x1a\n\x12\x65ms_real_acc_pedal\x18\n \x01(\x01\x12\x18\n\x10\x65ms_torq_failure\x18\x0b \x01(\r\x12\x1e\n\x16\x65ms_brake_pedal_status\x18\x0c \x01(\r\x12\x12\n\ntime_stamp\x18\r \x01(\x01\x12\x15\n\rmessage_valid\x18\x0e \x01(\r\x12\x11\n\treserved0\x18\x0f \x01(\r\x12\x11\n\treserved1\x18\x10 \x01(\rb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ems_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BUSEMS._serialized_start=23
  _BUSEMS._serialized_end=122
  _BUSEMSMOTIONINFO._serialized_start=125
  _BUSEMSMOTIONINFO._serialized_end=543
  _BUSEMSSTS._serialized_start=546
  _BUSEMSSTS._serialized_end=983
# @@protoc_insertion_point(module_scope)
