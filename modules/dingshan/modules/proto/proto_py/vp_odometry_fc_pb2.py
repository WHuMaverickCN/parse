# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vp_odometry_fc.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14vp_odometry_fc.proto\x12\x11VpOdometryFcProto\"A\n\x0bStablePitch\x12\r\n\x05pitch\x18\x01 \x01(\x02\x12\x10\n\x08is_valid\x18\x02 \x01(\x08\x12\x11\n\tis_jitter\x18\x03 \x01(\x08\"\xd0\x02\n\rOdometryFrame\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x07 \x01(\x02\x12\x0c\n\x04roll\x18\x08 \x01(\x02\x12\r\n\x05pitch\x18\t \x01(\x02\x12\x0b\n\x03yaw\x18\x03 \x01(\x02\x12\r\n\x05speed\x18\x04 \x01(\x02\x12\x10\n\x08yaw_rate\x18\x05 \x01(\x02\x12\x12\n\ntime_stamp\x18\x06 \x01(\x03\x12\x0e\n\x06source\x18\n \x01(\x05\x12\n\n\x02\x61x\x18\x0b \x01(\x02\x12\n\n\x02\x61y\x18\x0c \x01(\x02\x12\x13\n\x0bwheel_angle\x18\r \x01(\x02\x12\x0c\n\x04gear\x18\x0e \x01(\x05\x12\x34\n\x0cstable_pitch\x18\x0f \x01(\x0b\x32\x1e.VpOdometryFcProto.StablePitch\x12\x10\n\x08\x66rame_id\x18\x10 \x01(\x05\x12\x15\n\rwhl_spd_le_re\x18\x11 \x01(\x01\x12\x15\n\rwhl_spd_ri_re\x18\x12 \x01(\x01*\x82\x02\n\x0eOdometrySource\x12\x1b\n\x17OdometrySource_TWOWHEEL\x10\x01\x12\x1c\n\x18OdometrySource_FOURWHEEL\x10\x02\x12\x18\n\x14OdometrySource_SPEED\x10@\x12\x1b\n\x16OdometrySource_YAWRATE\x10\x80\x01\x12\"\n\x1dOdometrySource_STEERING_ANGLE\x10\x80\x02\x12\x1f\n\x1aOdometrySource_WHEEL_SPEED\x10\x80\x04\x12\x1f\n\x1aOdometrySource_WHEEL_PULSE\x10\x80\x08\x12\x18\n\x13OdometrySource_GEAR\x10\x80\x10')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vp_odometry_fc_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ODOMETRYSOURCE._serialized_start=450
  _ODOMETRYSOURCE._serialized_end=708
  _STABLEPITCH._serialized_start=43
  _STABLEPITCH._serialized_end=108
  _ODOMETRYFRAME._serialized_start=111
  _ODOMETRYFRAME._serialized_end=447
# @@protoc_insertion_point(module_scope)
