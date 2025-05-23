# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dynamic_layer.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import vp_ndm_base_v2_pb2 as vp__ndm__base__v2__pb2
import vp_obstacle_pb2 as vp__obstacle__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x64ynamic_layer.proto\x12\x0cVpNdmProtoV2\x1a\x14vp_ndm_base_v2.proto\x1a\x11vp_obstacle.proto\"\xfb\x03\n\x0fObjectAttribute\x12\x0b\n\x03rgb\x18\x01 \x03(\r\x12%\n\x03lwh\x18\x02 \x01(\x0b\x32\x13.VpNdmProtoV2.PointH\x00\x88\x01\x01\x12\'\n\nkey_points\x18\x05 \x03(\x0b\x32\x13.VpNdmProtoV2.Point\x12+\n\x0epolygon_points\x18\x06 \x03(\x0b\x32\x13.VpNdmProtoV2.Point\x12;\n\x04type\x18\x1e \x01(\x0e\x32(.VpNdmProtoV2.ObjectAttribute.ObjectTypeH\x01\x88\x01\x01\x12\x16\n\tclass_ind\x18\x1f \x01(\rH\x02\x88\x01\x01\x12\x17\n\naction_ind\x18  \x01(\rH\x03\x88\x01\x01\x12\x19\n\x0c\x62\x65havior_ind\x18! \x01(\rH\x04\x88\x01\x01\x12\x1a\n\rintention_ind\x18\" \x01(\rH\x05\x88\x01\x01\x12\x15\n\x08identity\x18( \x01(\tH\x06\x88\x01\x01\"D\n\nObjectType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07VEHICLE\x10\x01\x12\x0c\n\x08TWOWHEEL\x10\x02\x12\x0e\n\nPEDESTRIAN\x10\x03\x42\x06\n\x04_lwhB\x07\n\x05_typeB\x0c\n\n_class_indB\r\n\x0b_action_indB\x0f\n\r_behavior_indB\x10\n\x0e_intention_indB\x0b\n\t_identity\"f\n\x06Signal\x12\x12\n\x05stamp\x18\x01 \x01(\x04H\x00\x88\x01\x01\x12\x13\n\x06seq_id\x18\x02 \x01(\rH\x01\x88\x01\x01\x12\x13\n\x06signal\x18\n \x01(\rH\x02\x88\x01\x01\x42\x08\n\x06_stampB\t\n\x07_seq_idB\t\n\x07_signal\"\xb3\x01\n\x0eSignalSequence\x12\x0f\n\x02id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05stamp\x18\x02 \x01(\x04H\x01\x88\x01\x01\x12\x13\n\x06seq_id\x18\x03 \x01(\rH\x02\x88\x01\x01\x12\x16\n\tlife_time\x18\x04 \x01(\x02H\x03\x88\x01\x01\x12%\n\x07signals\x18\n \x03(\x0b\x32\x14.VpNdmProtoV2.SignalB\x05\n\x03_idB\x08\n\x06_stampB\t\n\x07_seq_idB\x0c\n\n_life_time\"\xc1\x03\n\x0eMoveableObject\x12\x0f\n\x02id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05stamp\x18\x02 \x01(\x04H\x01\x88\x01\x01\x12\x13\n\x06seq_id\x18\x03 \x01(\rH\x02\x88\x01\x01\x12\x16\n\tlife_time\x18\x04 \x01(\x02H\x03\x88\x01\x01\x12\x30\n\x04\x61ttr\x18\x08 \x01(\x0b\x32\x1d.VpNdmProtoV2.ObjectAttributeH\x04\x88\x01\x01\x12\x31\n\ntrajectory\x18\n \x01(\x0b\x32\x18.VpNdmProtoV2.TrajectoryH\x05\x88\x01\x01\x12\x35\n\x13predict_trajectorys\x18\x0b \x03(\x0b\x32\x18.VpNdmProtoV2.Trajectory\x12\x35\n\nsignal_seq\x18\x0c \x01(\x0b\x32\x1c.VpNdmProtoV2.SignalSequenceH\x06\x88\x01\x01\x12\x39\n\x13predict_signal_seqs\x18\r \x03(\x0b\x32\x1c.VpNdmProtoV2.SignalSequenceB\x05\n\x03_idB\x08\n\x06_stampB\t\n\x07_seq_idB\x0c\n\n_life_timeB\x07\n\x05_attrB\r\n\x0b_trajectoryB\r\n\x0b_signal_seq\"\x9d\x01\n\x15TrafficLightBulbState\x12\x12\n\x05stamp\x18\x01 \x01(\x04H\x00\x88\x01\x01\x12\x13\n\x06seq_id\x18\x02 \x01(\rH\x01\x88\x01\x01\x12\x12\n\x05\x63olor\x18\n \x01(\x05H\x02\x88\x01\x01\x12\x18\n\x0bis_flashing\x18\x0b \x01(\x08H\x03\x88\x01\x01\x42\x08\n\x06_stampB\t\n\x07_seq_idB\x08\n\x06_colorB\x0e\n\x0c_is_flashing\"\x9e\x02\n\x18TrafficLightBulbSequence\x12\x0f\n\x02id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05stamp\x18\x02 \x01(\x04H\x01\x88\x01\x01\x12\x13\n\x06seq_id\x18\x03 \x01(\rH\x02\x88\x01\x01\x12\x16\n\tlife_time\x18\x04 \x01(\x02H\x03\x88\x01\x01\x12*\n\x1d\x61ssociate_trafficlightbulb_id\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x38\n\x0b\x62ulb_states\x18\n \x03(\x0b\x32#.VpNdmProtoV2.TrafficLightBulbStateB\x05\n\x03_idB\x08\n\x06_stampB\t\n\x07_seq_idB\x0c\n\n_life_timeB \n\x1e_associate_trafficlightbulb_id\"\x97\x02\n\x18TrafficLightDynamicState\x12\x0f\n\x02id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05stamp\x18\x02 \x01(\x04H\x01\x88\x01\x01\x12\x13\n\x06seq_id\x18\x03 \x01(\rH\x02\x88\x01\x01\x12\x16\n\tlife_time\x18\x04 \x01(\x02H\x03\x88\x01\x01\x12&\n\x19\x61ssociate_trafficlight_id\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x39\n\tbulb_seqs\x18\n \x03(\x0b\x32&.VpNdmProtoV2.TrafficLightBulbSequenceB\x05\n\x03_idB\x08\n\x06_stampB\t\n\x07_seq_idB\x0c\n\n_life_timeB\x1c\n\x1a_associate_trafficlight_id\"\xfc\x01\n\x10ParkingSlotState\x12\x0f\n\x02id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05stamp\x18\x02 \x01(\x04H\x01\x88\x01\x01\x12\x13\n\x06seq_id\x18\x03 \x01(\rH\x02\x88\x01\x01\x12\x16\n\tlife_time\x18\x04 \x01(\x02H\x03\x88\x01\x01\x12%\n\x18\x61ssociate_parkingslot_id\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x18\n\x0bis_occupied\x18\n \x01(\x08H\x05\x88\x01\x01\x42\x05\n\x03_idB\x08\n\x06_stampB\t\n\x07_seq_idB\x0c\n\n_life_timeB\x1b\n\x19_associate_parkingslot_idB\x0e\n\x0c_is_occupied\"\xae\x01\n\x0bTrafficCone\x12\x0f\n\x02id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12*\n\x06\x62order\x18\x02 \x01(\x0b\x32\x15.VpNdmProtoV2.PolygonH\x01\x88\x01\x01\x12)\n\x06height\x18\x03 \x01(\x0b\x32\x14.VpNdmProtoV2.NumberH\x02\x88\x01\x01\x12\x11\n\x04type\x18\x04 \x01(\x05H\x03\x88\x01\x01\x42\x05\n\x03_idB\t\n\x07_borderB\t\n\x07_heightB\x07\n\x05_type\"\xdc\x01\n\x10\x43onstructionZone\x12\x0f\n\x02id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05stamp\x18\x02 \x01(\x04H\x01\x88\x01\x01\x12\x13\n\x06seq_id\x18\x03 \x01(\rH\x02\x88\x01\x01\x12\x16\n\tlife_time\x18\x04 \x01(\x02H\x03\x88\x01\x01\x12*\n\x06\x62order\x18\n \x01(\x0b\x32\x15.VpNdmProtoV2.PolygonH\x04\x88\x01\x01\x12\x15\n\rassociate_ids\x18\x0b \x03(\tB\x05\n\x03_idB\x08\n\x06_stampB\t\n\x07_seq_idB\x0c\n\n_life_timeB\t\n\x07_border\"\xda\x01\n\x0eRestrictedZone\x12\x0f\n\x02id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05stamp\x18\x02 \x01(\x04H\x01\x88\x01\x01\x12\x13\n\x06seq_id\x18\x03 \x01(\rH\x02\x88\x01\x01\x12\x16\n\tlife_time\x18\x04 \x01(\x02H\x03\x88\x01\x01\x12*\n\x06\x62order\x18\n \x01(\x0b\x32\x15.VpNdmProtoV2.PolygonH\x04\x88\x01\x01\x12\x15\n\rassociate_ids\x18\x0b \x03(\tB\x05\n\x03_idB\x08\n\x06_stampB\t\n\x07_seq_idB\x0c\n\n_life_timeB\t\n\x07_border\"\xfc\x01\n\tStaticODD\x12\x0f\n\x02id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x13\n\x06is_odd\x18\x02 \x01(\x08H\x01\x88\x01\x01\x12\x11\n\x04type\x18\x03 \x01(\rH\x02\x88\x01\x01\x12\x13\n\x06\x61\x63tion\x18\x04 \x01(\rH\x03\x88\x01\x01\x12\x13\n\x06reason\x18\x05 \x01(\x04H\x04\x88\x01\x01\x12!\n\x05links\x18\x06 \x03(\x0b\x32\x12.VpNdmProtoV2.Link\x12\x11\n\x04\x63onf\x18\x07 \x01(\x02H\x05\x88\x01\x01\x12\x12\n\x05stamp\x18\x08 \x01(\x04H\x06\x88\x01\x01\x42\x05\n\x03_idB\t\n\x07_is_oddB\x07\n\x05_typeB\t\n\x07_actionB\t\n\x07_reasonB\x07\n\x05_confB\x08\n\x06_stamp\"s\n\x0cTrafficEvent\x12\x0f\n\x02id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x18\n\x0breliability\x18\x03 \x01(\rH\x01\x88\x01\x01\x12!\n\x05links\x18\x04 \x03(\x0b\x32\x12.VpNdmProtoV2.LinkB\x05\n\x03_idB\x0e\n\x0c_reliability\"r\n\x0bTrafficFlow\x12\x0f\n\x02id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x18\n\x0breliability\x18\x03 \x01(\rH\x01\x88\x01\x01\x12!\n\x05links\x18\x04 \x03(\x0b\x32\x12.VpNdmProtoV2.LinkB\x05\n\x03_idB\x0e\n\x0c_reliability\"\xa6\x04\n\x0c\x44ynamicLayer\x12\x36\n\x10moveable_objects\x18\x01 \x03(\x0b\x32\x1c.VpNdmProtoV2.MoveableObject\x12\x43\n\x13trafficlight_states\x18\x02 \x03(\x0b\x32&.VpNdmProtoV2.TrafficLightDynamicState\x12:\n\x12parkingslot_states\x18\x03 \x03(\x0b\x32\x1e.VpNdmProtoV2.ParkingSlotState\x12:\n\x12\x63onstruction_zones\x18\x04 \x03(\x0b\x32\x1e.VpNdmProtoV2.ConstructionZone\x12\x35\n\x0frestricted_zone\x18\x05 \x03(\x0b\x32\x1c.VpNdmProtoV2.RestrictedZone\x12(\n\x05\x63ones\x18\x06 \x03(\x0b\x32\x19.VpNdmProtoV2.TrafficCone\x12,\n\x0bstatic_odds\x18\x07 \x03(\x0b\x32\x17.VpNdmProtoV2.StaticODD\x12\x32\n\x0etraffic_events\x18\x08 \x03(\x0b\x32\x1a.VpNdmProtoV2.TrafficEvent\x12\x30\n\rtraffic_flows\x18\t \x03(\x0b\x32\x19.VpNdmProtoV2.TrafficFlow\x12,\n\tobstacles\x18\n \x03(\x0b\x32\x19.VpObstacleProto.Obstacleb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dynamic_layer_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _OBJECTATTRIBUTE._serialized_start=79
  _OBJECTATTRIBUTE._serialized_end=586
  _OBJECTATTRIBUTE_OBJECTTYPE._serialized_start=424
  _OBJECTATTRIBUTE_OBJECTTYPE._serialized_end=492
  _SIGNAL._serialized_start=588
  _SIGNAL._serialized_end=690
  _SIGNALSEQUENCE._serialized_start=693
  _SIGNALSEQUENCE._serialized_end=872
  _MOVEABLEOBJECT._serialized_start=875
  _MOVEABLEOBJECT._serialized_end=1324
  _TRAFFICLIGHTBULBSTATE._serialized_start=1327
  _TRAFFICLIGHTBULBSTATE._serialized_end=1484
  _TRAFFICLIGHTBULBSEQUENCE._serialized_start=1487
  _TRAFFICLIGHTBULBSEQUENCE._serialized_end=1773
  _TRAFFICLIGHTDYNAMICSTATE._serialized_start=1776
  _TRAFFICLIGHTDYNAMICSTATE._serialized_end=2055
  _PARKINGSLOTSTATE._serialized_start=2058
  _PARKINGSLOTSTATE._serialized_end=2310
  _TRAFFICCONE._serialized_start=2313
  _TRAFFICCONE._serialized_end=2487
  _CONSTRUCTIONZONE._serialized_start=2490
  _CONSTRUCTIONZONE._serialized_end=2710
  _RESTRICTEDZONE._serialized_start=2713
  _RESTRICTEDZONE._serialized_end=2931
  _STATICODD._serialized_start=2934
  _STATICODD._serialized_end=3186
  _TRAFFICEVENT._serialized_start=3188
  _TRAFFICEVENT._serialized_end=3303
  _TRAFFICFLOW._serialized_start=3305
  _TRAFFICFLOW._serialized_end=3419
  _DYNAMICLAYER._serialized_start=3422
  _DYNAMICLAYER._serialized_end=3972
# @@protoc_insertion_point(module_scope)
