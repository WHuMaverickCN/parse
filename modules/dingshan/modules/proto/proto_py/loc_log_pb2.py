# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: loc_log.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import loc_trigger_pb2 as loc__trigger__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rloc_log.proto\x12\x0clocalization\x1a\x11loc_trigger.proto\"A\n\x03Log\x12,\n\nadrtrigger\x18\x01 \x01(\x0b\x32\x18.localization.LocTrigger\x12\x0c\n\x04logs\x18\x02 \x01(\t\"\x9f\x01\n\x10LocDiagnosisInfo\x12\x12\n\ntime_stamp\x18\x01 \x01(\x01\x12\x19\n\x11\x66ront_module_fail\x18\x02 \x01(\r\x12\x1c\n\x14input_signal_invalid\x18\x03 \x01(\r\x12\x1c\n\x14module_running_error\x18\x04 \x01(\r\x12\x0e\n\x06is_dtc\x18\x05 \x01(\r\x12\x10\n\x08reserved\x18\x06 \x01(\x01*\x92\x01\n\rDiagnosisType\x12\x11\n\rkTimeSynFault\x10\x00\x12\x0f\n\x0bkInsTimeout\x10\x01\x12\x0e\n\nkFcTimeout\x10\x02\x12\x11\n\rkHdmapTimeout\x10\x03\x12\x10\n\x0ckFcDataFault\x10\x04\x12\x13\n\x0fkHdmapDataFault\x10\x05\x12\x13\n\x0fkWheelDataDault\x10\x06\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'loc_log_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DIAGNOSISTYPE._serialized_start=280
  _DIAGNOSISTYPE._serialized_end=426
  _LOG._serialized_start=50
  _LOG._serialized_end=115
  _LOCDIAGNOSISINFO._serialized_start=118
  _LOCDIAGNOSISINFO._serialized_end=277
# @@protoc_insertion_point(module_scope)
