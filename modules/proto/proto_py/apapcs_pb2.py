# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: apapcs.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ca_apa_slot_sector_pb2 as ca__apa__slot__sector__pb2
import seq_header_pb2 as seq__header__pb2
import fusion_common_pb2 as fusion__common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x61papcs.proto\x12\x06\x61papcs\x1a\x18\x63\x61_apa_slot_sector.proto\x1a\x10seq_header.proto\x1a\x13\x66usion_common.proto\"\x8e\x01\n\tPathPoint\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\x0f\n\x07heading\x18\x03 \x01(\x01\x12\x11\n\tcurvature\x18\x04 \x01(\x01\x12\t\n\x01s\x18\x05 \x01(\x01\x12\x15\n\rleft_boundary\x18\x06 \x01(\x02\x12\x16\n\x0eright_boundary\x18\x07 \x01(\x02\x12\r\n\x05slope\x18\x08 \x01(\x02\"\x8f\x01\n\x08Maneuver\x12!\n\x06points\x18\x01 \x03(\x0b\x32\x11.apapcs.PathPoint\x12\x13\n\x0btarget_gear\x18\x02 \x01(\r\x12#\n\x06source\x18\x03 \x01(\x0e\x32\x13.apapcs.ManeuverSrc\x12\x0e\n\x06length\x18\x04 \x01(\x01\x12\x16\n\x0emaneuver_index\x18\x05 \x01(\r\"Z\n\rSamplingPoint\x12!\n\x06points\x18\x01 \x01(\x0b\x32\x11.apapcs.PathPoint\x12\x0c\n\x04\x63ost\x18\x02 \x01(\x04\x12\x0b\n\x03row\x18\x03 \x01(\r\x12\x0b\n\x03\x63ol\x18\x04 \x01(\r\"4\n\x0bSamplingMap\x12%\n\x06points\x18\x01 \x03(\x0b\x32\x15.apapcs.SamplingPoint\"c\n\x0bParkingPath\x12/\n\x0fplanning_status\x18\x01 \x01(\x0e\x32\x16.apapcs.PlanningStatus\x12#\n\tmaneuvers\x18\x02 \x03(\x0b\x32\x10.apapcs.Maneuver\"\x1e\n\x06Pose2D\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\"C\n\x08GridCell\x12\"\n\ncenter_pnt\x18\x01 \x01(\x0b\x32\x0e.apapcs.Pose2D\x12\x13\n\x0bis_occupied\x18\x02 \x01(\x08\"F\n\x0fGridMapProperty\x12\x11\n\tcoord_res\x18\x01 \x01(\x01\x12\x0f\n\x07\x63ol_num\x18\x02 \x01(\x01\x12\x0f\n\x07row_num\x18\x03 \x01(\x01\"Z\n\x07GridMap\x12$\n\ngrid_cells\x18\x01 \x03(\x0b\x32\x10.apapcs.GridCell\x12)\n\x08property\x18\x02 \x01(\x0b\x32\x17.apapcs.GridMapProperty\"w\n\x0bParkingSlot\x12 \n\x08vertices\x18\x01 \x03(\x0b\x32\x0e.apapcs.Pose2D\x12\x1f\n\x07limiter\x18\x02 \x03(\x0b\x32\x0e.apapcs.Pose2D\x12%\n\rparking_space\x18\x03 \x03(\x0b\x32\x0e.apapcs.Pose2D\"p\n\x0c\x44\x65\x62ugCluster\x12!\n\tstart_pnt\x18\x01 \x01(\x0b\x32\x0e.apapcs.Pose2D\x12\x1f\n\x07\x65nd_pnt\x18\x02 \x01(\x0b\x32\x0e.apapcs.Pose2D\x12\x0e\n\x06height\x18\x03 \x01(\x01\x12\x0c\n\x04type\x18\x04 \x01(\x05\"\xba\x03\n\x08\x44\x65\x62ugMsg\x12!\n\x08grid_map\x18\x01 \x01(\x0b\x32\x0f.apapcs.GridMap\x12!\n\tfreespace\x18\x02 \x03(\x0b\x32\x0e.apapcs.Pose2D\x12#\n\x08\x65go_pose\x18\x03 \x01(\x0b\x32\x11.apapcs.PathPoint\x12\"\n\x05slots\x18\x04 \x03(\x0b\x32\x13.apapcs.ParkingSlot\x12(\n\x0btarget_slot\x18\x05 \x01(\x0b\x32\x13.apapcs.ParkingSlot\x12)\n\x0cparking_path\x18\x06 \x01(\x0b\x32\x13.apapcs.ParkingPath\x12%\n\ntarget_pnt\x18\x07 \x01(\x0b\x32\x11.apapcs.PathPoint\x12%\n\x07\x63luster\x18\x08 \x03(\x0b\x32\x14.apapcs.DebugCluster\x12%\n\nerror_type\x18\t \x03(\x0e\x32\x11.apapcs.ErrorType\x12)\n\x0cwarning_type\x18\n \x03(\x0e\x32\x13.apapcs.WarningType\x12\x15\n\rapa_diagnosis\x18\x0b \x01(\x04\x12\x13\n\x0b\x61pa_version\x18\x0c \x01(\t\"%\n\x07\x44iySlot\x12\x1a\n\x12\x64iy_slot_available\x18\x01 \x01(\r\"\xcd\x02\n\rPlanningState\x12\x12\n\nsearch_num\x18\x01 \x01(\r\x12/\n\x0f\x61nalytical_path\x18\x02 \x01(\x0e\x32\x16.apapcs.LatPlannerType\x12/\n\x0fplanning_status\x18\x03 \x01(\x0e\x32\x16.apapcs.PlanningStatus\x12\x1e\n\x16\x64ist_frm_crnt_manuever\x18\x04 \x01(\x01\x12\x16\n\x0e\x64\x65st_pnt_error\x18\x05 \x01(\x01\x12\x18\n\x10\x63urrent_manuever\x18\x06 \x01(\r\x12\"\n\x1a\x63urrent_manuever_match_idx\x18\x07 \x01(\r\x12\x19\n\x11\x61papcs_heart_beat\x18\x08 \x01(\r\x12\x10\n\x08plan_num\x18\t \x01(\r\x12#\n\tpath_info\x18\n \x01(\x0b\x32\x10.apapcs.PathInfo\"}\n\x07LatPlan\x12\x0c\n\x04\x65yaw\x18\x01 \x01(\x05\x12\x0c\n\x04\x65pos\x18\x02 \x01(\x05\x12\x0c\n\x04tarc\x18\x03 \x01(\x05\x12/\n\nseq_header\x18\x04 \x01(\x0b\x32\x1b.SeqHeaderProto.DelayHeader\x12\x17\n\x0fsteer_angle_req\x18\x05 \x01(\x01\"\xbb\x02\n\x08LongPlan\x12\x13\n\x0btarget_dist\x18\x01 \x01(\x05\x12\x14\n\x0ctarget_speed\x18\x02 \x01(\r\x12\x11\n\tpt_status\x18\x03 \x01(\r\x12\x0b\n\x03\x64tc\x18\x04 \x01(\x05\x12\x0b\n\x03\x64th\x18\x05 \x01(\x05\x12\x12\n\nmoving_dir\x18\x06 \x01(\x05\x12\x13\n\x0btarget_gear\x18\x07 \x01(\r\x12\r\n\x05pitch\x18\x08 \x01(\x01\x12\x30\n\x10lon_planner_type\x18\t \x01(\x0e\x32\x16.apapcs.LonPlannerType\x12/\n\nseq_header\x18\n \x01(\x0b\x32\x1b.SeqHeaderProto.DelayHeader\x12%\n\nspeed_type\x18\x0b \x01(\x0e\x32\x11.apapcs.SpeedType\x12\x15\n\rdtc_safe_dist\x18\x0c \x01(\r\"z\n\x13RecommendedFunction\x12/\n\x11\x66unction_released\x18\x01 \x03(\x0e\x32\x14.apapcs.FunctionType\x12\x32\n\x14\x66unction_recommended\x18\x02 \x01(\x0e\x32\x14.apapcs.FunctionType\"N\n\x14ParkInRecommendation\x12\x19\n\x11released_slots_id\x18\x01 \x03(\x05\x12\x1b\n\x13recommended_slot_id\x18\x02 \x01(\x05\"n\n\x15ParkOutRecommendation\x12(\n\x0creleased_dir\x18\x01 \x03(\x0e\x32\x12.apapcs.ParkingDir\x12+\n\x0frecommended_dir\x18\x02 \x01(\x0e\x32\x12.apapcs.ParkingDir\"\xda\x01\n\x12ParkRecommendation\x12+\n\rfunction_type\x18\x01 \x01(\x0e\x32\x14.apapcs.FunctionType\x12>\n\x16park_in_recommendation\x18\x02 \x01(\x0b\x32\x1c.apapcs.ParkInRecommendationH\x00\x12@\n\x17park_out_recommendation\x18\x03 \x01(\x0b\x32\x1d.apapcs.ParkOutRecommendationH\x00\x42\x15\n\x13park_recommendation\"\xe1\x01\n\x0fRecommendedInfo\x12\x39\n\x14recommended_function\x18\x01 \x01(\x0b\x32\x1b.apapcs.RecommendedFunction\x12\x37\n\x13park_recommendation\x18\x02 \x01(\x0b\x32\x1a.apapcs.ParkRecommendation\x12)\n\npcs_notice\x18\x03 \x03(\x0e\x32\x15.apapcs.PcsNoticeType\x12/\n\nseq_header\x18\x04 \x01(\x0b\x32\x1b.SeqHeaderProto.DelayHeader\"\xc7\x01\n\nParkInDcsn\x12-\n\x0e\x64\x65\x63ision_state\x18\x01 \x01(\x0e\x32\x15.apapcs.DecisionState\x12\'\n\x0ctarget_point\x18\x02 \x01(\x0b\x32\x11.apapcs.PathPoint\x12\x33\n\x0btarget_slot\x18\x03 \x01(\x0b\x32\x1e.CaApaSlotSectorProto.SlotInfo\x12,\n\x11target_point_base\x18\x04 \x01(\x0b\x32\x11.apapcs.PathPoint\"\xf8\x01\n\x0bParkOutDcsn\x12-\n\x0e\x64\x65\x63ision_state\x18\x01 \x01(\x0e\x32\x15.apapcs.DecisionState\x12\'\n\x0ctarget_point\x18\x02 \x01(\x0b\x32\x11.apapcs.PathPoint\x12.\n\x12target_parking_dir\x18\x03 \x01(\x0e\x32\x12.apapcs.ParkingDir\x12\x33\n\x0btarget_slot\x18\x04 \x01(\x0b\x32\x1e.CaApaSlotSectorProto.SlotInfo\x12,\n\x11target_point_base\x18\x05 \x01(\x0b\x32\x11.apapcs.PathPoint\"\x86\x06\n\x0e\x44\x65\x63isionResult\x12+\n\rfunction_type\x18\x01 \x01(\x0e\x32\x14.apapcs.FunctionType\x12*\n\x0cpark_in_dcsn\x18\x02 \x01(\x0b\x32\x12.apapcs.ParkInDcsnH\x00\x12,\n\rpark_out_dcsn\x18\x03 \x01(\x0b\x32\x13.apapcs.ParkOutDcsnH\x00\x12\x18\n\x10planning_trigger\x18\x04 \x01(\x08\x12-\n\x0e\x64\x65\x63ision_state\x18\x05 \x01(\x0e\x32\x15.apapcs.DecisionState\x12\'\n\x0ctarget_point\x18\x06 \x01(\x0b\x32\x11.apapcs.PathPoint\x12\x1e\n\x16park_out_takeover_dcsn\x18\x07 \x01(\x08\x12\'\n\tcase_type\x18\x08 \x01(\x0e\x32\x14.apapcs.ParkCaseType\x12#\n\tstep_type\x18\t \x01(\x0e\x32\x10.apapcs.StepType\x12.\n\x13\x61rbitrate_loc_point\x18\n \x01(\x0b\x32\x11.apapcs.PathPoint\x12\x32\n\x11\x61pa_scenario_type\x18\x0b \x01(\x0e\x32\x17.apapcs.ApaScenarioType\x12>\n\x17\x63ourtesy_obstacles_type\x18\x0c \x01(\x0e\x32\x1d.apapcs.CourtesyObstaclesType\x12H\n\x1dstraight_in_out_safe_distance\x18\r \x01(\x0e\x32!.apapcs.StraightInOutSafeDistance\x12&\n\rdiy_slot_dcsn\x18\x0e \x01(\x0b\x32\x0f.apapcs.DiySlot\x12/\n\nseq_header\x18\x0f \x01(\x0b\x32\x1b.SeqHeaderProto.DelayHeader\x12\x18\n\x10\x64\x61ta_to_file_sts\x18\x10 \x01(\r\x12 \n\x18rearview_mirror_flod_sts\x18\x11 \x01(\rB\n\n\x08\x64\x63sn_res\"\x8d\x0f\n\x11\x41\x64\x64tionalDebugMsg\x12%\n\rparking_space\x18\x01 \x03(\x0b\x32\x0e.apapcs.Pose2D\x12?\n\x18parallel_knead_slot_info\x18\x02 \x01(\x0b\x32\x1d.apapcs.ParallelKneadSlotInfo\x12\x30\n\x15plan_start_pnt_latest\x18\x03 \x01(\x0b\x32\x11.apapcs.PathPoint\x12.\n\x13plan_end_pnt_latest\x18\x04 \x01(\x0b\x32\x11.apapcs.PathPoint\x12\x32\n\x17\x65scape_start_pnt_latest\x18\x05 \x01(\x0b\x32\x11.apapcs.PathPoint\x12\x30\n\x15\x65scape_end_pnt_latest\x18\x06 \x01(\x0b\x32\x11.apapcs.PathPoint\x12&\n\x0btrack_error\x18\x07 \x01(\x0b\x32\x11.apapcs.PathPoint\x12+\n\x10target_pnt_error\x18\x08 \x01(\x0b\x32\x11.apapcs.PathPoint\x12\x1a\n\x12target_slot_length\x18\t \x01(\x01\x12\x19\n\x11target_slot_width\x18\n \x01(\x01\x12\x18\n\x10target_slot_side\x18\x0b \x01(\x05\x12\x13\n\x0bplan_enable\x18\x0c \x01(\x08\x12\x15\n\rreplan_enable\x18\r \x01(\x08\x12\x1b\n\x13\x64ynamic_plan_enable\x18\x0e \x01(\x08\x12\x13\n\x0b\x66\x61iled_task\x18\x0f \x03(\r\x12\x12\n\napa_active\x18\x10 \x01(\x08\x12\x16\n\x0egoal_collision\x18\x11 \x01(\x08\x12\x18\n\x10\x64istance_reached\x18\x12 \x01(\x08\x12\x17\n\x0fheading_reached\x18\x13 \x01(\x08\x12\x18\n\x10no_replan_reason\x18\x14 \x01(\r\x12\x15\n\rreplan_reason\x18\x15 \x01(\r\x12 \n\x18special_parking_property\x18\x16 \x01(\r\x12\x1a\n\x12special_target_pnt\x18\x17 \x01(\r\x12\x13\n\x0bpath_length\x18\x18 \x01(\x01\x12\x15\n\rmin_dtc_index\x18\x19 \x01(\r\x12\x19\n\x11\x64ynamic_obst_type\x18\x1a \x01(\r\x12\x13\n\x0brs_seg_type\x18\x1b \x03(\r\x12\x15\n\rrs_seg_length\x18\x1c \x03(\x01\x12\x19\n\x11park_space_length\x18\x1d \x01(\x01\x12\x18\n\x10park_space_width\x18\x1e \x01(\x01\x12*\n\x0ftp_left_ref_pnt\x18\x1f \x01(\x0b\x32\x11.apapcs.PathPoint\x12+\n\x10tp_right_ref_pnt\x18  \x01(\x0b\x32\x11.apapcs.PathPoint\x12,\n\x11tp_bottom_ref_pnt\x18! \x01(\x0b\x32\x11.apapcs.PathPoint\x12\x19\n\x11tp_failure_reason\x18\" \x01(\r\x12 \n\x18path_plan_failure_reason\x18# \x01(\r\x12)\n\x0elook_ahead_pnt\x18$ \x01(\x0b\x32\x11.apapcs.PathPoint\x12\x16\n\x0eis_ego_in_slot\x18% \x01(\x08\x12\x19\n\x11\x64tc_safe_distance\x18& \x01(\r\x12\x16\n\x0eis_ego_on_ramp\x18\' \x01(\x08\x12\x33\n\x11\x64riving_condition\x18( \x01(\x0e\x32\x18.apapcs.DrivingCondition\x12\x1c\n\x14sector_warning_limit\x18) \x03(\x01\x12$\n\x1cvelocity_restriction_by_path\x18* \x01(\x01\x12%\n\x1dvelocity_restriction_by_colli\x18+ \x01(\x01\x12\'\n\x1fvelocity_restriction_in_advance\x18, \x01(\x01\x12$\n\x1cmin_dist_for_plan_in_advance\x18- \x01(\x01\x12&\n\x1epedestrian_distance_to_vehicle\x18. \x01(\x01\x12\x36\n\x13spacing_pile_status\x18/ \x01(\x0e\x32\x19.apapcs.SpacingPileStatus\x12\x12\n\nramp_slope\x18\x30 \x01(\x01\x12\x19\n\x11plan_trigger_type\x18\x31 \x01(\r\x12\x1a\n\x12plan_failed_reason\x18\x32 \x01(\r\x12(\n dynamic_connection_failed_reason\x18\x33 \x01(\r\x12\x1f\n\x17non_parking_over_reason\x18\x34 \x01(\r\x12\'\n\x1fvelocity_restricton_by_dist_map\x18\x35 \x01(\x01\x12\x1c\n\x14min_dist_in_dist_map\x18\x36 \x01(\x01\x12(\n velocity_restricton_by_curvature\x18\x37 \x01(\x01\x12\x1e\n\x16preview_mean_curvature\x18\x38 \x01(\x01\x12\x1e\n\x16\x63urrent_mean_curvature\x18\x39 \x01(\x01\"f\n\x0c\x41paDiagnosis\x12\x12\n\ntime_stamp\x18\x01 \x01(\x01\x12\x16\n\x0e\x64iagnosis_code\x18\x02 \x01(\r\x12\x16\n\x0e\x64iagnosis_info\x18\x03 \x01(\t\x12\x12\n\nheart_beat\x18\x04 \x01(\r\"\xf8\x01\n\x15ParallelKneadSlotInfo\x12\x1b\n\x13\x66lag_knead_slot_run\x18\x01 \x01(\x08\x12\x13\n\x0b\x66lag_sucess\x18\x02 \x01(\x08\x12\x19\n\x11\x66lag_has_raw_path\x18\x03 \x01(\x08\x12\x1c\n\x14\x66lag_has_filter_path\x18\x04 \x01(\x08\x12\x18\n\x10knead_slot_count\x18\x05 \x01(\r\x12+\n\x10\x64r_feature_point\x18\x06 \x01(\x0b\x32\x11.apapcs.PathPoint\x12-\n\x12slot_feature_point\x18\x07 \x01(\x0b\x32\x11.apapcs.PathPoint\"3\n\x14\x41papcsStateSwitchRsp\x12\x1b\n\x13\x61papcs_sts_feedback\x18\x01 \x01(\r\"\x96\x01\n\x08PathInfo\x12\x13\n\x0bpath_status\x18\x01 \x01(\r\x12\x11\n\tpd_status\x18\x02 \x01(\r\x12\x19\n\x11pd_sub_apa_status\x18\x03 \x01(\r\x12+\n\x0fparking_out_dir\x18\x04 \x01(\x0e\x32\x12.apapcs.ParkingDir\x12\x1a\n\x12parking_in_slot_id\x18\x05 \x01(\x05\"\xe1\x01\n\nHzpNavInfo\x12\x13\n\x0b\x63ruise_road\x18\x01 \x01(\r\x12\x1c\n\x14\x64ist_to_barrier_gate\x18\x02 \x01(\x01\x12\x14\n\x0c\x64ist_to_slop\x18\x03 \x01(\x01\x12\x1c\n\x14\x64ist_to_intersection\x18\x04 \x01(\x01\x12\x19\n\x11\x64ist_to_left_turn\x18\x05 \x01(\x01\x12\x1a\n\x12\x64ist_to_right_turn\x18\x06 \x01(\x01\x12\x18\n\x10\x64ist_to_ref_line\x18\x07 \x01(\x01\x12\x1b\n\x13refline_remain_dist\x18\x08 \x01(\x01\"\x9d\x03\n\x18HzpBehaviourDecisionInfo\x12%\n\x1dis_in_path_avoidance_scenario\x18\x01 \x01(\x08\x12 \n\x18\x66ront_static_obstacle_id\x18\x02 \x01(\r\x12\x1d\n\x15voidance_over_counter\x18\x03 \x01(\r\x12#\n\x1b\x64\x65\x63ided_avoidance_direction\x18\x04 \x01(\x08\x12%\n\x1dis_in_path_following_scenario\x18\x05 \x01(\x08\x12\x1b\n\x13\x66ollowing_object_id\x18\x06 \x01(\r\x12#\n\x1bis_in_path_meeting_scenario\x18\x07 \x01(\x08\x12\x19\n\x11meeting_object_id\x18\x08 \x01(\r\x12\x11\n\treserve_1\x18\t \x01(\x01\x12\x11\n\treserve_2\x18\n \x01(\x01\x12\x11\n\treserve_3\x18\x0b \x01(\x01\x12\x11\n\treserve_4\x18\x0c \x01(\x01\x12\x11\n\treserve_5\x18\r \x01(\x01\x12\x11\n\treserve_6\x18\x0e \x01(\x01\"i\n\x0fHzpDecisionInfo\x12\x12\n\nhzp_status\x18\x01 \x01(\r\x12\x10\n\x08hzp_mode\x18\x02 \x01(\r\x12\x1a\n\x12target_slot_status\x18\x03 \x01(\r\x12\x14\n\x0c\x63ruise_scene\x18\x04 \x01(\r\";\n\x12PredictedTrajPoint\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\x0f\n\x07heading\x18\x03 \x01(\x01\"b\n\rPredictedTraj\x12\x12\n\nconfidence\x18\x01 \x01(\x02\x12*\n\x06points\x18\x02 \x03(\x0b\x32\x1a.apapcs.PredictedTrajPoint\x12\x11\n\ttime_step\x18\x03 \x01(\x02\"\xa6\x06\n\x0fPredictedObject\x12\x10\n\x08track_id\x18\x01 \x01(\x05\x12\x0e\n\x06length\x18\x02 \x01(\x02\x12\r\n\x05width\x18\x03 \x01(\x02\x12\x15\n\rheading_angle\x18\x04 \x01(\x02\x12\x36\n\x0e\x63lassification\x18\x05 \x01(\x0e\x32\x1e.FusionCommonProto.ObjectClass\x12\x15\n\rdetect_sensor\x18\x06 \x01(\r\x12\x12\n\nconfidence\x18\x07 \x01(\x05\x12\x0b\n\x03\x61ge\x18\x08 \x01(\x05\x12\x17\n\x0f\x63ross_line_flag\x18\t \x01(\x08\x12\x18\n\x10\x63ross_line_value\x18\n \x01(\x02\x12\x34\n\x06status\x18\x0b \x01(\x0e\x32$.FusionCommonProto.ObjectMotionState\x12\x1d\n\x15longitudinal_distance\x18\x0c \x01(\x02\x12\x18\n\x10lateral_distance\x18\r \x01(\x02\x12&\n\x1elongitudinal_absolute_velocity\x18\x0e \x01(\x02\x12!\n\x19lateral_absolute_velocity\x18\x0f \x01(\x02\x12&\n\x1elongitudinal_relative_velocity\x18\x10 \x01(\x02\x12!\n\x19lateral_relative_velocity\x18\x11 \x01(\x02\x12<\n\x10obj_refer_points\x18\x12 \x03(\x0b\x32\".FusionCommonProto.Point2DPosition\x12\x32\n\x0bturn_signal\x18\x13 \x01(\x0e\x32\x1d.FusionCommonProto.TurnSignal\x12\x33\n\x0b\x62rake_light\x18\x14 \x01(\x0e\x32\x1e.FusionCommonProto.BrakeSignal\x12\x13\n\x0b\x63over_level\x18\x15 \x01(\x05\x12\x15\n\rmoving_status\x18\x16 \x01(\x05\x12\x12\n\nmoving_dir\x18\x17 \x01(\x05\x12\x16\n\x0epredictor_type\x18\x18 \x01(\x05\x12$\n\x05trajs\x18\x19 \x03(\x0b\x32\x15.apapcs.PredictedTraj\"N\n\x13HzpPredictedObjects\x12\x10\n\x08\x66rame_id\x18\x01 \x01(\r\x12%\n\x04objs\x18\x02 \x03(\x0b\x32\x17.apapcs.PredictedObject*Y\n\x0ePlanningStatus\x12\x1c\n\x18PLANNNING_STATUS_UNKNOWN\x10\x00\x12\x14\n\x10PLANNING_SUCCESS\x10\x01\x12\x13\n\x0fPLANNING_FAILED\x10\x02*\xae\x01\n\x0bManeuverSrc\x12\x18\n\x14MANEUVER_SRC_UNKNOWN\x10\x00\x12\x17\n\x13MANEUVER_SRC_SEARCH\x10\x01\x12\x1e\n\x1aMANEUVER_SRC_ANALYTICAL_RS\x10\x02\x12$\n MANEUVER_SRC_ANALYTICAL_GEOMETRY\x10\x03\x12&\n\"MANEUVER_SRC_ANALYTICAL_CONNECTION\x10\x04*\xea\x02\n\x0eLatPlannerType\x12\x1b\n\x17PARKING_PLANNER_UNKNOWN\x10\x00\x12\x10\n\x0cHYBRID_ASTAR\x10\x01\x12\x0e\n\nRS_PLANNER\x10\x02\x12\x0c\n\x08GEOMETRY\x10\x03\x12\x0e\n\nCONNECTION\x10\x04\x12\x10\n\x0c\x41\x43R_GEOMETRY\x10\x05\x12\n\n\x06\x45SCAPE\x10\x06\x12\x0b\n\x07MIXTURE\x10\x07\x12\n\n\x06\x41\x44JUST\x10\x08\x12\x0b\n\x07PARK_IN\x10\t\x12\x0f\n\x0b\x41\x44JUST_BASE\x10\n\x12\x17\n\x13PARALLEL_OUT_ADJUST\x10\x0b\x12\x12\n\x0eREVERSE_ASSIST\x10\x0c\x12\x1b\n\x17STRAIGHT_IN_OUT_PLANNER\x10\r\x12\x16\n\x12HZP_CRUISE_PLANNER\x10\x0e\x12\x17\n\x13HYBRID_ASTAR_CRUISE\x10\x0f\x12\x07\n\x03\x44WA\x10\x10\x12\x0f\n\x0bREVERSE_ARC\x10\x11\x12\x11\n\rSTATE_LATTICE\x10\x12*\xa0\x01\n\x0eLonPlannerType\x12\x17\n\x13LON_PLANNER_UNKNOWN\x10\x00\x12\x13\n\x0fLON_PLANNER_OLD\x10\x01\x12\x13\n\x0fLON_PLANNER_NEW\x10\x02\x12\x1a\n\x16LON_PLANNER_PROTECTION\x10\x03\x12\x1a\n\x16LON_PLANNER_PREDICTION\x10\x04\x12\x13\n\x0fLON_PLANNER_HZP\x10\x05*e\n\tSpeedType\x12\x17\n\x13SPEED_TYPE_INACTIVE\x10\x00\x12\x13\n\x0fSPEED_TYPE_SLOW\x10\x01\x12\x15\n\x11SPEED_TYPE_NORMAL\x10\x02\x12\x13\n\x0fSPEED_TYPE_FAST\x10\x03*\x84\x02\n\x0c\x46unctionType\x12\x14\n\x10\x46UNCTION_UNKNOWN\x10\x00\x12\x1b\n\x17\x46UNCTION_PARK_IN_INSIDE\x10\x01\x12\x1c\n\x18\x46UNCTION_PARK_IN_OUTSIDE\x10\x02\x12\x15\n\x11\x46UNCTION_PARK_OUT\x10\x03\x12\x1c\n\x18\x46UNCTION_STRAIGHT_IN_OUT\x10\x04\x12\x0f\n\x0b\x46UNCTION_RA\x10\x05\x12\x18\n\x14\x46UNCTION_HZP_PARK_IN\x10\x06\x12\x17\n\x13\x46UNCTION_HZP_SUMMON\x10\x07\x12\x10\n\x0c\x46UNCTION_AVP\x10\x08\x12\x18\n\x14\x46UNCTION_REMOTE_PARK\x10\t*{\n\x0f\x41paScenarioType\x12\x17\n\x13\x41PA_SENARIO_UNKNOWN\x10\x00\x12\x17\n\x13\x41PA_SENARIO_WARNING\x10\x01\x12\x1e\n\x1a\x41PA_SENARIO_TEMPORARY_STOP\x10\x02\x12\x16\n\x12\x41PA_SENARIO_NORMAL\x10\x03*\xec\x01\n\nParkingDir\x12\x17\n\x13PARKING_DIR_UNKNOWN\x10\x00\x12\x14\n\x10PARKING_DIR_LEFT\x10\x01\x12\x15\n\x11PARKING_DIR_RIGHT\x10\x02\x12!\n\x1dPARKING_DIR_STRAIGHT_FOREWARD\x10\x03\x12!\n\x1dPARKING_DIR_STRAIGHT_BACKWARD\x10\x04\x12\x19\n\x15PARKING_DIR_LEFT_REAR\x10\x05\x12\x1a\n\x16PARKING_DIR_RIGHT_REAR\x10\x06\x12\x1b\n\x17PARKING_DIR_UNAVAILABLE\x10\x07*v\n\x15\x43ourtesyObstaclesType\x12\x1e\n\x1a\x43OURTESY_OBSTACLES_UNKNOWN\x10\x00\x12\x1d\n\x19\x43OURTESY_OBSTACLES_PEOPLE\x10\x01\x12\x1e\n\x1a\x43OURTESY_OBSTACLES_VEHICLE\x10\x02*\xa9\x01\n\x19StraightInOutSafeDistance\x12\"\n\x1eREACHING_SAFE_DISTANCE_UNKNOWN\x10\x00\x12\"\n\x1eREACHING_SAFE_DISTANCE_FORWARD\x10\x01\x12#\n\x1fREACHING_SAFE_DISTANCE_BACKWARD\x10\x02\x12\x1f\n\x1bREACHING_SAFE_DISTANCE_SIDE\x10\x03*q\n\rPcsNoticeType\x12\x15\n\x11PCS_NOTICE_UNKOWN\x10\x00\x12\x14\n\x10SLOT_UNAVAILABLE\x10\x01\x12\x19\n\x15PARK_OUT_SPACE_NARROW\x10\x02\x12\x18\n\x14PARK_IN_SPACE_NARROW\x10\x03*\xa7\x01\n\rDecisionState\x12\x11\n\rDECISION_INIT\x10\x00\x12\x15\n\x11\x44\x45\x43ISION_PLANNING\x10\x01\x12\x1d\n\x19\x44\x45\x43ISION_PLANNING_SUCCESS\x10\x02\x12\x1c\n\x18\x44\x45\x43ISION_PLANNING_FAILED\x10\x03\x12\x14\n\x10\x44\x45\x43ISION_PARKING\x10\x04\x12\x19\n\x15\x44\x45\x43ISION_PARKING_OVER\x10\x05*\xe8\x01\n\x10\x44rivingCondition\x12\x13\n\x0f\x44RIVING_UNKNOWN\x10\x00\x12\x18\n\x14\x44RIVING_LEFT_FORWARD\x10\x01\x12\x1c\n\x18\x44RIVING_STRAIGHT_FORWARD\x10\x02\x12\x19\n\x15\x44RIVING_RIGHT_FORWARD\x10\x03\x12\x19\n\x15\x44RIVING_LEFT_BACKWARD\x10\x04\x12\x1d\n\x19\x44RIVING_STRAIGHT_BACKWARD\x10\x05\x12\x1a\n\x16\x44RIVING_RIGHT_BACKWARD\x10\x06\x12\x16\n\x12\x44RIVING_STANDSTILL\x10\x07*\xab\x01\n\x11SpacingPileStatus\x12\x10\n\x0cPILE_UNKNOWN\x10\x00\x12\x14\n\x10PILE_NEED_REPLAN\x10\x01\x12-\n)PILE_NEED_REPLAN_PARALLEL_SPECIAL_PARK_IN\x10\x02\x12\x0f\n\x0bPILE_FINISH\x10\x03\x12.\n*PILE_NEED_REPLAN_PARALLEL_SPECIAL_PARK_OUT\x10\x04*\xd2\x03\n\tErrorType\x12\x14\n\x10\x45RROR_NOT_HAPPEN\x10\x00\x12\x14\n\x10\x45RROR_NOT_UNKOWN\x10\x01\x12\x16\n\x12\x45RROR_NO_FREESPACE\x10\x02\x12\x19\n\x15\x45RROR_NO_PARKING_SLOT\x10\x03\x12\x1e\n\x1a\x45RROR_LOCALIZATION_INVALID\x10\x04\x12\x1d\n\x19\x45RROR_HZP_MAP_UNAVAILABLE\x10\x05\x12$\n ERROR_REFERENCE_LINE_UNAVAILABLE\x10\x06\x12\x17\n\x13\x45RROR_SEARCH_FAILED\x10\x07\x12\x19\n\x15\x45RROR_LAT_PLAN_FAILED\x10\x08\x12\x18\n\x14\x45RROR_NO_LAT_PLANNER\x10\t\x12\x18\n\x14\x45RROR_NO_LON_PLANNER\x10\n\x12!\n\x1d\x45RROR_TARGET_SLOT_UNAVAILABLE\x10\x0b\x12\x1d\n\x19\x45RROR_RELEASED_SLOT_EMPTY\x10\x0c\x12#\n\x1f\x45RROR_RELEASED_SLOT_UNAVAILABLE\x10\r\x12\x17\n\x13\x45RROR_ADJUST_FAILED\x10\x0e\x12\x19\n\x15\x45RROR_LON_PLAN_FAILED\x10\x0f*\xdb\x01\n\x0bWarningType\x12\x16\n\x12WARNING_NOT_HAPPEN\x10\x00\x12 \n\x1cWARNING_LAT_PLANNING_TIMEOUT\x10\x01\x12 \n\x1cWARNING_LON_PLANNING_TIMEOUT\x10\x02\x12\x1c\n\x18WARNING_TARGET_COLLISION\x10\x03\x12\x15\n\x11WARNING_NO_TARGET\x10\x04\x12\x19\n\x15WARNING_SMOOTH_FAILED\x10\x05\x12 \n\x1cWARNING_PARKING_SPACE_FAILED\x10\x0e*\x9f\x03\n\x0cParkCaseType\x12\x10\n\x0c\x43\x41SE_UNKNOWN\x10\x00\x12 \n\x1c\x43\x41SE_PARK_IN_PARALLEL_NORMAL\x10\x01\x12%\n!CASE_PARK_IN_PARALLEL_INSIDE_SLOT\x10\x02\x12 \n\x1c\x43\x41SE_PARK_IN_VERTICAL_NORMAL\x10\x03\x12%\n!CASE_PARK_IN_VERTICAL_INSIDE_SLOT\x10\x04\x12\x1a\n\x16\x43\x41SE_PARK_OUT_PARALLEL\x10\x05\x12\x1a\n\x16\x43\x41SE_PARK_OUT_VERTICAL\x10\x06\x12\x1b\n\x17\x43\x41SE_DYNAMIC_CONNECTION\x10\x07\x12\x18\n\x14\x43\x41SE_PARK_IN_ANGULAR\x10\x08\x12\x10\n\x0c\x43\x41SE_REVERSE\x10\t\x12\x16\n\x12\x43\x41SE_CRUISE_NORMAL\x10\n\x12\x19\n\x15\x43\x41SE_PARK_OUT_ANGULAR\x10\x0b\x12\x1d\n\x19\x43\x41SE_PARK_IN_SELF_DEFINED\x10\x0c\x12\x18\n\x14\x43\x41SE_STRAIGHT_IN_OUT\x10\r*\xd0\x01\n\x08StepType\x12\x10\n\x0cSTEP_UNKNOWN\x10\x00\x12\x17\n\x13STEP_PARK_IN_NORMAL\x10\x01\x12\x1b\n\x17STEP_PARK_IN_CONNECTION\x10\x02\x12\x17\n\x13STEP_PARK_IN_ADJUST\x10\x03\x12\x18\n\x14STEP_PARK_OUT_NORMAL\x10\x04\x12\x17\n\x13STEP_REVERSE_ASSIST\x10\x05\x12\x18\n\x14STEP_STRAIGHT_IN_OUT\x10\x06\x12\x16\n\x12STEP_CRUISE_NORMAL\x10\x07\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'apapcs_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PLANNINGSTATUS._serialized_start=8685
  _PLANNINGSTATUS._serialized_end=8774
  _MANEUVERSRC._serialized_start=8777
  _MANEUVERSRC._serialized_end=8951
  _LATPLANNERTYPE._serialized_start=8954
  _LATPLANNERTYPE._serialized_end=9316
  _LONPLANNERTYPE._serialized_start=9319
  _LONPLANNERTYPE._serialized_end=9479
  _SPEEDTYPE._serialized_start=9481
  _SPEEDTYPE._serialized_end=9582
  _FUNCTIONTYPE._serialized_start=9585
  _FUNCTIONTYPE._serialized_end=9845
  _APASCENARIOTYPE._serialized_start=9847
  _APASCENARIOTYPE._serialized_end=9970
  _PARKINGDIR._serialized_start=9973
  _PARKINGDIR._serialized_end=10209
  _COURTESYOBSTACLESTYPE._serialized_start=10211
  _COURTESYOBSTACLESTYPE._serialized_end=10329
  _STRAIGHTINOUTSAFEDISTANCE._serialized_start=10332
  _STRAIGHTINOUTSAFEDISTANCE._serialized_end=10501
  _PCSNOTICETYPE._serialized_start=10503
  _PCSNOTICETYPE._serialized_end=10616
  _DECISIONSTATE._serialized_start=10619
  _DECISIONSTATE._serialized_end=10786
  _DRIVINGCONDITION._serialized_start=10789
  _DRIVINGCONDITION._serialized_end=11021
  _SPACINGPILESTATUS._serialized_start=11024
  _SPACINGPILESTATUS._serialized_end=11195
  _ERRORTYPE._serialized_start=11198
  _ERRORTYPE._serialized_end=11664
  _WARNINGTYPE._serialized_start=11667
  _WARNINGTYPE._serialized_end=11886
  _PARKCASETYPE._serialized_start=11889
  _PARKCASETYPE._serialized_end=12304
  _STEPTYPE._serialized_start=12307
  _STEPTYPE._serialized_end=12515
  _PATHPOINT._serialized_start=90
  _PATHPOINT._serialized_end=232
  _MANEUVER._serialized_start=235
  _MANEUVER._serialized_end=378
  _SAMPLINGPOINT._serialized_start=380
  _SAMPLINGPOINT._serialized_end=470
  _SAMPLINGMAP._serialized_start=472
  _SAMPLINGMAP._serialized_end=524
  _PARKINGPATH._serialized_start=526
  _PARKINGPATH._serialized_end=625
  _POSE2D._serialized_start=627
  _POSE2D._serialized_end=657
  _GRIDCELL._serialized_start=659
  _GRIDCELL._serialized_end=726
  _GRIDMAPPROPERTY._serialized_start=728
  _GRIDMAPPROPERTY._serialized_end=798
  _GRIDMAP._serialized_start=800
  _GRIDMAP._serialized_end=890
  _PARKINGSLOT._serialized_start=892
  _PARKINGSLOT._serialized_end=1011
  _DEBUGCLUSTER._serialized_start=1013
  _DEBUGCLUSTER._serialized_end=1125
  _DEBUGMSG._serialized_start=1128
  _DEBUGMSG._serialized_end=1570
  _DIYSLOT._serialized_start=1572
  _DIYSLOT._serialized_end=1609
  _PLANNINGSTATE._serialized_start=1612
  _PLANNINGSTATE._serialized_end=1945
  _LATPLAN._serialized_start=1947
  _LATPLAN._serialized_end=2072
  _LONGPLAN._serialized_start=2075
  _LONGPLAN._serialized_end=2390
  _RECOMMENDEDFUNCTION._serialized_start=2392
  _RECOMMENDEDFUNCTION._serialized_end=2514
  _PARKINRECOMMENDATION._serialized_start=2516
  _PARKINRECOMMENDATION._serialized_end=2594
  _PARKOUTRECOMMENDATION._serialized_start=2596
  _PARKOUTRECOMMENDATION._serialized_end=2706
  _PARKRECOMMENDATION._serialized_start=2709
  _PARKRECOMMENDATION._serialized_end=2927
  _RECOMMENDEDINFO._serialized_start=2930
  _RECOMMENDEDINFO._serialized_end=3155
  _PARKINDCSN._serialized_start=3158
  _PARKINDCSN._serialized_end=3357
  _PARKOUTDCSN._serialized_start=3360
  _PARKOUTDCSN._serialized_end=3608
  _DECISIONRESULT._serialized_start=3611
  _DECISIONRESULT._serialized_end=4385
  _ADDTIONALDEBUGMSG._serialized_start=4388
  _ADDTIONALDEBUGMSG._serialized_end=6321
  _APADIAGNOSIS._serialized_start=6323
  _APADIAGNOSIS._serialized_end=6425
  _PARALLELKNEADSLOTINFO._serialized_start=6428
  _PARALLELKNEADSLOTINFO._serialized_end=6676
  _APAPCSSTATESWITCHRSP._serialized_start=6678
  _APAPCSSTATESWITCHRSP._serialized_end=6729
  _PATHINFO._serialized_start=6732
  _PATHINFO._serialized_end=6882
  _HZPNAVINFO._serialized_start=6885
  _HZPNAVINFO._serialized_end=7110
  _HZPBEHAVIOURDECISIONINFO._serialized_start=7113
  _HZPBEHAVIOURDECISIONINFO._serialized_end=7526
  _HZPDECISIONINFO._serialized_start=7528
  _HZPDECISIONINFO._serialized_end=7633
  _PREDICTEDTRAJPOINT._serialized_start=7635
  _PREDICTEDTRAJPOINT._serialized_end=7694
  _PREDICTEDTRAJ._serialized_start=7696
  _PREDICTEDTRAJ._serialized_end=7794
  _PREDICTEDOBJECT._serialized_start=7797
  _PREDICTEDOBJECT._serialized_end=8603
  _HZPPREDICTEDOBJECTS._serialized_start=8605
  _HZPPREDICTEDOBJECTS._serialized_end=8683
# @@protoc_insertion_point(module_scope)
