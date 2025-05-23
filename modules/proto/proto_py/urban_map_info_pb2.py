# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: urban_map_info.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import header_pb2 as header__pb2
import urban_map_common_pb2 as urban__map__common__pb2
import odometry_pb2 as odometry__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14urban_map_info.proto\x12\x0clocalization\x1a\x0cheader.proto\x1a\x16urban_map_common.proto\x1a\x0eodometry.proto\"\xf0\x02\n\rUrbanMapLists\x12$\n\x06header\x18\x01 \x01(\x0b\x32\x14.localization.Header\x12\x43\n\rid_to_mapinfo\x18\x02 \x03(\x0b\x32,.localization.UrbanMapLists.IdToMapinfoEntry\x12\x15\n\rtotal_map_num\x18\x03 \x01(\r\x12\x1f\n\x17total_favority_slot_num\x18\x04 \x01(\r\x12\x1a\n\x12total_map_distance\x18\x05 \x01(\x01\x12\x19\n\x11total_parking_num\x18\x06 \x01(\r\x12\x12\n\nreserved_1\x18\x07 \x01(\x01\x12\x12\n\nreserved_2\x18\x08 \x01(\r\x12\x12\n\nreserved_3\x18\t \x01(\t\x1aI\n\x10IdToMapinfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.localization.MapInfo:\x02\x38\x01\"\xb3\x02\n\x0f\x43omponentStatus\x12$\n\x06header\x18\x01 \x01(\x0b\x32\x14.localization.Header\x12\x12\n\ncs_running\x18\x02 \x01(\x08\x12\'\n\x08map_info\x18\x03 \x01(\x0b\x32\x15.localization.MapInfo\x12\x37\n\x0cstudy_status\x18\x04 \x01(\x0e\x32!.localization.UrbanMapStudyStatus\x12+\n\numm_status\x18\x05 \x01(\x0e\x32\x17.localization.UmmStatus\x12+\n\nerror_type\x18\x06 \x01(\x0e\x32\x17.localization.ErrorType\x12\x14\n\x0cstatus_res_1\x18\x07 \x01(\r\x12\x14\n\x0cstatus_res_2\x18\x08 \x01(\t\"\x87\x02\n\x0cUrbanMapInfo\x12$\n\x06header\x18\x01 \x01(\x0b\x32\x14.localization.Header\x12)\n\tinfo_type\x18\x02 \x01(\x0e\x32\x16.localization.InfoType\x12-\n\rmap_learn_req\x18\x03 \x01(\x0e\x32\x16.localization.LearnReq\x12\'\n\x08map_info\x18\x04 \x01(\x0b\x32\x15.localization.MapInfo\x12\x12\n\nmap_update\x18\x05 \x01(\x08\x12\x12\n\nreserved_1\x18\x06 \x01(\x01\x12\x12\n\nreserved_2\x18\x07 \x01(\r\x12\x12\n\nreserved_3\x18\x08 \x01(\t\"\xd2\x03\n\x07MapInfo\x12\x0e\n\x06map_id\x18\x01 \x01(\t\x12\x11\n\tmap_alias\x18\x02 \x01(\t\x12\x10\n\x08map_path\x18\x03 \x01(\t\x12\x10\n\x08map_time\x18\x04 \x01(\t\x12\x10\n\x08utc_time\x18\x05 \x01(\x01\x12\x0c\n\x04pace\x18\x06 \x01(\x01\x12\x32\n\x0eurban_map_type\x18\x07 \x01(\x0e\x32\x1a.localization.UrbanMapType\x12\x35\n\rpark_map_type\x18\x08 \x01(\x0e\x32\x1e.localization.ParkUrbanMapType\x12\x38\n\x0fparking_element\x18\t \x01(\x0b\x32\x1f.localization.ParkingElementNum\x12\x34\n\rmap_dist_info\x18\n \x01(\x0b\x32\x1d.localization.MapDistanceInfo\x12\x34\n\x0cmap_loc_info\x18\x0b \x01(\x0b\x32\x1e.localization.UrbanMapLocation\x12\x13\n\x0busage_times\x18\x0c \x01(\r\x12\x12\n\nreserved_1\x18\r \x01(\x01\x12\x12\n\nreserved_2\x18\x0e \x01(\r\x12\x12\n\nreserved_3\x18\x0f \x01(\t\"\xa4\x01\n\x11RealMappingStatus\x12\'\n\x08map_info\x18\x01 \x01(\x0b\x32\x15.localization.MapInfo\x12\x39\n\x0emapping_status\x18\x02 \x01(\x0e\x32!.localization.UrbanMapStudyStatus\x12+\n\nerror_type\x18\x03 \x01(\x0e\x32\x17.localization.ErrorType\"\xae\x01\n\x07GpsBias\x12$\n\x06header\x18\x01 \x01(\x0b\x32\x14.localization.Header\x12\x12\n\nvalid_flag\x18\x02 \x01(\x08\x12\x16\n\x0elongitude_bias\x18\x03 \x01(\x01\x12\x15\n\rlatitude_bias\x18\x04 \x01(\x01\x12\x12\n\nreserved_1\x18\x05 \x01(\x01\x12\x12\n\nreserved_2\x18\x06 \x01(\r\x12\x12\n\nreserved_3\x18\x07 \x01(\t\"\xcf\x01\n\x11ParkingElementNum\x12\x15\n\rcurr_slot_num\x18\x01 \x01(\r\x12\x1e\n\x16\x63urr_favority_slot_num\x18\x03 \x01(\r\x12\x1b\n\x13\x63urr_speed_bump_num\x18\x05 \x01(\r\x12\x10\n\x08ramp_num\x18\x06 \x01(\r\x12\x18\n\x10\x63urrent_floor_id\x18\x07 \x01(\t\x12\x12\n\nreserved_1\x18\x08 \x01(\x01\x12\x12\n\nreserved_2\x18\t \x01(\r\x12\x12\n\nreserved_3\x18\n \x01(\t\"s\n\x0fMapDistanceInfo\x12\x1a\n\x12\x63urrent_study_dist\x18\x01 \x01(\x01\x12\x1c\n\x14\x63urrent_map_distance\x18\x02 \x01(\x01\x12\x12\n\nreserved_1\x18\x03 \x01(\x01\x12\x12\n\nreserved_2\x18\x04 \x01(\r\"\xc0\x01\n\x10UrbanMapLocation\x12,\n\x0flearn_start_ins\x18\x01 \x01(\x0b\x32\x13.localization.Point\x12*\n\rlearn_end_ins\x18\x02 \x01(\x0b\x32\x13.localization.Point\x12)\n\x0csd_start_loc\x18\x03 \x01(\x0b\x32\x13.localization.Point\x12\'\n\nsd_end_loc\x18\x04 \x01(\x0b\x32\x13.localization.Pointb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'urban_map_info_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _URBANMAPLISTS_IDTOMAPINFOENTRY._options = None
  _URBANMAPLISTS_IDTOMAPINFOENTRY._serialized_options = b'8\001'
  _URBANMAPLISTS._serialized_start=93
  _URBANMAPLISTS._serialized_end=461
  _URBANMAPLISTS_IDTOMAPINFOENTRY._serialized_start=388
  _URBANMAPLISTS_IDTOMAPINFOENTRY._serialized_end=461
  _COMPONENTSTATUS._serialized_start=464
  _COMPONENTSTATUS._serialized_end=771
  _URBANMAPINFO._serialized_start=774
  _URBANMAPINFO._serialized_end=1037
  _MAPINFO._serialized_start=1040
  _MAPINFO._serialized_end=1506
  _REALMAPPINGSTATUS._serialized_start=1509
  _REALMAPPINGSTATUS._serialized_end=1673
  _GPSBIAS._serialized_start=1676
  _GPSBIAS._serialized_end=1850
  _PARKINGELEMENTNUM._serialized_start=1853
  _PARKINGELEMENTNUM._serialized_end=2060
  _MAPDISTANCEINFO._serialized_start=2062
  _MAPDISTANCEINFO._serialized_end=2177
  _URBANMAPLOCATION._serialized_start=2180
  _URBANMAPLOCATION._serialized_end=2372
# @@protoc_insertion_point(module_scope)
