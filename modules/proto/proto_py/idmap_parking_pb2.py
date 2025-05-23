# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: idmap_parking.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import idmap_common_pb2 as idmap__common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13idmap_parking.proto\x12\x05idmap\x1a\x12idmap_common.proto\"\xf7\x01\n\x0bParkingInfo\x12\x12\n\nparking_id\x18\x01 \x01(\x04\x12\x14\n\x0cparking_name\x18\x02 \x01(\x0c\x12\x14\n\x0cparking_type\x18\x03 \x01(\x05\x12\x14\n\x0c\x66loors_total\x18\x04 \x01(\x05\x12\x13\n\x0bslots_total\x18\x05 \x01(\x05\x12\x1c\n\x14parking_limit_height\x18\x06 \x01(\x01\x12\x0f\n\x07\x61\x64\x64ress\x18\x07 \x01(\x0c\x12\x10\n\x08province\x18\x08 \x01(\x0c\x12\x0c\n\x04\x63ity\x18\t \x01(\x0c\x12\x10\n\x08\x64istrict\x18\n \x01(\x0c\x12\x1c\n\x14having_charging_pile\x18\x0b \x01(\x08\"\xa9\x01\n\x11\x46loorAndRampGroup\x12\x0e\n\x06\x66rg_id\x18\x01 \x01(\x04\x12\x14\n\x0cis_rampgroup\x18\x02 \x01(\x08\x12\x13\n\x0b\x66loor_level\x18\x03 \x01(\x05\x12\x10\n\x08\x66rg_name\x18\x04 \x01(\t\x12+\n\x0eparking_blocks\x18\x05 \x03(\x0b\x32\x13.idmap.ParkingBlock\x12\x1a\n\x12\x61ssociated_lane_id\x18\x06 \x03(\x04\"k\n\x0cParkingBlock\x12\x18\n\x10parking_block_id\x18\x01 \x01(\x04\x12\x1a\n\x12parking_block_name\x18\x02 \x01(\x0c\x12%\n\x10\x62lock_point_list\x18\x03 \x03(\x0b\x32\x0b.idmap.Gnss\"8\n\x0bParkingLane\x12\x18\n\x10lane_hight_limit\x18\x01 \x01(\x01\x12\x0f\n\x07lane_id\x18\x02 \x01(\x04\"\xfc\x01\n\x0bParkingSlot\x12\x0f\n\x07slot_id\x18\x01 \x01(\x04\x12\x11\n\tslot_code\x18\x02 \x01(\x0c\x12\x11\n\tslot_type\x18\x03 \x01(\r\x12\x16\n\x0eslot_direction\x18\x04 \x01(\r\x12\x11\n\tyaw_angle\x18\x05 \x01(\x01\x12\x1b\n\x13\x61ssociated_floor_id\x18\x06 \x01(\x04\x12\x14\n\x0cslot_lock_id\x18\x07 \x01(\x04\x12\x17\n\x0fslot_limiter_id\x18\x08 \x01(\x04\x12$\n\x0fslot_corner_pts\x18\t \x03(\x0b\x32\x0b.idmap.Gnss\x12\x19\n\x11slot_corner_logic\x18\n \x03(\r\"\x97\x02\n\x0bParkingGate\x12\x17\n\x0fparking_gate_id\x18\x01 \x01(\x04\x12\x19\n\x11parking_gate_name\x18\x02 \x01(\x0c\x12\x19\n\x11parking_gate_type\x18\x03 \x01(\x05\x12\x1b\n\x13\x61ssociated_lane_ids\x18\x04 \x03(\x04\x12\x1b\n\x13\x61ssociated_floor_id\x18\x05 \x01(\x04\x12\x1f\n\ngnss_point\x18\x06 \x01(\x0b\x32\x0b.idmap.Gnss\x12\x1e\n\x16original_coordinates_x\x18\x07 \x01(\x01\x12\x1e\n\x16original_coordinates_y\x18\x08 \x01(\x01\x12\x1e\n\x16original_coordinates_z\x18\t \x01(\x01\"\xaf\x01\n\x07\x42\x61rrier\x12\x12\n\nbarrier_id\x18\x01 \x01(\x04\x12\x14\n\x0c\x62\x61rrier_type\x18\x02 \x01(\x05\x12\x1b\n\x13\x61ssociated_lane_ids\x18\x03 \x03(\x04\x12\x1b\n\x13\x61ssociated_floor_id\x18\x04 \x01(\x04\x12(\n\x13geometry_point_list\x18\x05 \x03(\x0b\x32\x0b.idmap.Gnss\x12\x16\n\x0e\x62\x61rrier_height\x18\x06 \x01(\x05\"\xad\x01\n\x11\x41vpMapTrafficSign\x12\x16\n\x0e\x61vpmap_sign_id\x18\x01 \x01(\x04\x12\x10\n\x08\x66unction\x18\x02 \x01(\r\x12\x13\n\x0bis_variable\x18\x03 \x01(\x08\x12\x16\n\x0e\x61ngle_to_north\x18\x04 \x01(\x01\x12\x19\n\x11\x61vpmap_sign_color\x18\x05 \x01(\r\x12&\n\x11\x61vpmap_sign_point\x18\x06 \x03(\x0b\x32\x0b.idmap.Gnss\"\x81\x01\n\x0bWallMarking\x12\x17\n\x0fwall_marking_id\x18\x01 \x01(\x04\x12\x19\n\x11wall_marking_type\x18\x02 \x01(\x05\x12\x1a\n\x12wall_marking_color\x18\x03 \x01(\r\x12\"\n\rwm_point_list\x18\x04 \x03(\x0b\x32\x0b.idmap.Gnss\"\x99\x01\n\x08\x46\x61\x63ility\x12\x13\n\x0b\x66\x61\x63ility_id\x18\x01 \x01(\x04\x12\x15\n\rfacility_type\x18\x02 \x01(\x05\x12\x1a\n\x12\x61ssociated_lane_id\x18\x03 \x03(\x04\x12\x1b\n\x13\x61ssociated_floor_id\x18\x04 \x01(\x04\x12(\n\x13geometry_point_list\x18\x05 \x03(\x0b\x32\x0b.idmap.Gnss\"v\n\x03POI\x12\x0e\n\x06poi_id\x18\x01 \x01(\x04\x12\x10\n\x08poi_type\x18\x02 \x01(\x05\x12\x1b\n\x13\x61ssociated_lane_ids\x18\x03 \x03(\x04\x12\x1e\n\tpoi_point\x18\x04 \x01(\x0b\x32\x0b.idmap.Gnss\x12\x10\n\x08poi_name\x18\x05 \x01(\x0c\"b\n\x04Polo\x12\x0f\n\x07polo_id\x18\x01 \x01(\x04\x12\x11\n\tpolo_type\x18\x02 \x01(\r\x12\x15\n\rpolo_diameter\x18\x03 \x01(\x01\x12\x1f\n\npolo_point\x18\x04 \x01(\x0b\x32\x0b.idmap.Gnss\"\xfa\x03\n\x0fPakingIDMapInfo\x12(\n\x0cparking_info\x18\x01 \x01(\x0b\x32\x12.idmap.ParkingInfo\x12,\n\nfloor_ramp\x18\x02 \x03(\x0b\x32\x18.idmap.FloorAndRampGroup\x12(\n\x0cparking_lane\x18\x03 \x03(\x0b\x32\x12.idmap.ParkingLane\x12)\n\rparking_slots\x18\x04 \x03(\x0b\x32\x12.idmap.ParkingSlot\x12)\n\rparking_gates\x18\x05 \x03(\x0b\x32\x12.idmap.ParkingGate\x12 \n\x08\x62\x61rriers\x18\x06 \x03(\x0b\x32\x0e.idmap.Barrier\x12\x36\n\x14\x61vpmap_traffic_signs\x18\x07 \x03(\x0b\x32\x18.idmap.AvpMapTrafficSign\x12(\n\x0cwall_marking\x18\x08 \x03(\x0b\x32\x12.idmap.WallMarking\x12#\n\nfacilities\x18\t \x03(\x0b\x32\x0f.idmap.Facility\x12\x18\n\x04pois\x18\n \x03(\x0b\x32\n.idmap.POI\x12!\n\x0cparking_polo\x18\x0b \x03(\x0b\x32\x0b.idmap.Polo\x12\x14\n\x0cpath_lane_id\x18\x0c \x03(\x04\x12\x13\n\x0bstatus_code\x18\r \x01(\rb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'idmap_parking_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PARKINGINFO._serialized_start=51
  _PARKINGINFO._serialized_end=298
  _FLOORANDRAMPGROUP._serialized_start=301
  _FLOORANDRAMPGROUP._serialized_end=470
  _PARKINGBLOCK._serialized_start=472
  _PARKINGBLOCK._serialized_end=579
  _PARKINGLANE._serialized_start=581
  _PARKINGLANE._serialized_end=637
  _PARKINGSLOT._serialized_start=640
  _PARKINGSLOT._serialized_end=892
  _PARKINGGATE._serialized_start=895
  _PARKINGGATE._serialized_end=1174
  _BARRIER._serialized_start=1177
  _BARRIER._serialized_end=1352
  _AVPMAPTRAFFICSIGN._serialized_start=1355
  _AVPMAPTRAFFICSIGN._serialized_end=1528
  _WALLMARKING._serialized_start=1531
  _WALLMARKING._serialized_end=1660
  _FACILITY._serialized_start=1663
  _FACILITY._serialized_end=1816
  _POI._serialized_start=1818
  _POI._serialized_end=1936
  _POLO._serialized_start=1938
  _POLO._serialized_end=2036
  _PAKINGIDMAPINFO._serialized_start=2039
  _PAKINGIDMAPINFO._serialized_end=2545
# @@protoc_insertion_point(module_scope)
