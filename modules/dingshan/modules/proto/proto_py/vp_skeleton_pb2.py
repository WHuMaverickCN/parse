# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vp_skeleton.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import vp_obstacle_raw_pb2 as vp__obstacle__raw__pb2
import vp_perception_base_pb2 as vp__perception__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11vp_skeleton.proto\x12\x0fVpSkeletonProto\x1a\x15vp_obstacle_raw.proto\x1a\x18vp_perception_base.proto\"H\n\rSkeletonPoint\x12(\n\x02pt\x18\x01 \x01(\x0b\x32\x1c.VpPerceptionBaseProto.Point\x12\r\n\x05valid\x18\x02 \x01(\x05\"H\n\x08Skeleton\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x30\n\x08skeleton\x18\x02 \x03(\x0b\x32\x1e.VpSkeletonProto.SkeletonPoint\"q\n\x0bSkeletonRaw\x12\x30\n\x07percept\x18\x01 \x01(\x0b\x32\x1f.VpObstacleRawProto.ObstacleRaw\x12\x30\n\x08skeleton\x18\x02 \x03(\x0b\x32\x1e.VpSkeletonProto.SkeletonPoint\"R\n\x0cSkeletonRaws\x12\x0e\n\x06\x63\x61m_id\x18\x01 \x01(\x05\x12\x32\n\x0cskeleton_raw\x18\x02 \x03(\x0b\x32\x1c.VpSkeletonProto.SkeletonRaw*\xf5\x03\n\x0cSkeletonType\x12\x15\n\x11SkeletonType_nose\x10\x00\x12\x19\n\x15SkeletonType_left_eye\x10\x01\x12\x1a\n\x16SkeletonType_right_eye\x10\x02\x12\x19\n\x15SkeletonType_left_ear\x10\x03\x12\x1a\n\x16SkeletonType_right_ear\x10\x04\x12\x1e\n\x1aSkeletonType_left_shoulder\x10\x05\x12\x1f\n\x1bSkeletonType_right_shoulder\x10\x06\x12\x1b\n\x17SkeletonType_left_elbow\x10\x07\x12\x1c\n\x18SkeletonType_right_elbow\x10\x08\x12\x1b\n\x17SkeletonType_left_wrist\x10\t\x12\x1c\n\x18SkeletonType_right_wrist\x10\n\x12\x19\n\x15SkeletonType_left_hip\x10\x0b\x12\x1a\n\x16SkeletonType_right_hip\x10\x0c\x12\x1a\n\x16SkeletonType_left_knee\x10\r\x12\x1b\n\x17SkeletonType_right_knee\x10\x0e\x12\x1b\n\x17SkeletonType_left_ankle\x10\x0f\x12\x1c\n\x18SkeletonType_right_ankle\x10\x10')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vp_skeleton_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SKELETONTYPE._serialized_start=435
  _SKELETONTYPE._serialized_end=936
  _SKELETONPOINT._serialized_start=87
  _SKELETONPOINT._serialized_end=159
  _SKELETON._serialized_start=161
  _SKELETON._serialized_end=233
  _SKELETONRAW._serialized_start=235
  _SKELETONRAW._serialized_end=348
  _SKELETONRAWS._serialized_start=350
  _SKELETONRAWS._serialized_end=432
# @@protoc_insertion_point(module_scope)
