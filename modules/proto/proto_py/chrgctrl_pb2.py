# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chrgctrl.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x63hrgctrl.proto\x12\rChrgCtrlProto\"\xbe\x01\n\x08\x43hrgCtrl\x12\x12\n\ntime_stamp\x18\x01 \x01(\x01\x12\x31\n\rchrg_tip_info\x18\x02 \x01(\x0b\x32\x1a.ChrgCtrlProto.ChrgTipInfo\x12\x38\n\x11obc_chrg_inp_outp\x18\x03 \x01(\x0b\x32\x1d.ChrgCtrlProto.ObcChrgInpOutp\x12\x31\n\rchrg_ctrl_sts\x18\x04 \x01(\x0b\x32\x1a.ChrgCtrlProto.ChrgCtrlSts\"\xc1\x01\n\x0b\x43hrgTipInfo\x12\x12\n\ntime_stamp\x18\x01 \x01(\x01\x12\x18\n\x10\x62\x63u_chrg_ti_disp\x18\x02 \x01(\r\x12\x18\n\x10\x62\x63u_chrg_ti_pred\x18\x03 \x01(\r\x12\x19\n\x11\x62\x63u_text_disp_req\x18\x04 \x01(\r\x12\x1c\n\x14\x62\x63u_dc_text_disp_req\x18\x05 \x01(\r\x12\x1a\n\x12vcu_chrg_text_disp\x18\x06 \x01(\r\x12\x15\n\rmessage_valid\x18\x07 \x01(\r\"\x9d\x02\n\x0eObcChrgInpOutp\x12\x12\n\ntime_stamp\x18\x01 \x01(\x01\x12\x1c\n\x14obc_chrg_inp_ac_u_l1\x18\x02 \x01(\r\x12\x1c\n\x14obc_chrg_inp_ac_u_l2\x18\x03 \x01(\r\x12\x1c\n\x14obc_chrg_inp_ac_u_l3\x18\x04 \x01(\r\x12\x1c\n\x14obc_chrg_inp_ac_i_l1\x18\x05 \x01(\r\x12\x1c\n\x14obc_chrg_inp_ac_i_l2\x18\x06 \x01(\r\x12\x1c\n\x14obc_chrg_inp_ac_i_l3\x18\x07 \x01(\r\x12\x15\n\robc_chrg_dc_i\x18\x08 \x01(\r\x12\x15\n\robc_chrg_dc_u\x18\t \x01(\r\x12\x15\n\rmessage_valid\x18\n \x01(\r\"\xb5\x01\n\x0b\x43hrgCtrlSts\x12\x12\n\ntime_stamp\x18\x01 \x01(\x01\x12\x19\n\x11vcu_chrg_sts_lamp\x18\x02 \x01(\r\x12\x1b\n\x13vcu_veh_chrg_sts_gb\x18\x03 \x01(\r\x12\x14\n\x0c\x62\x63u_chrg_mod\x18\x04 \x01(\r\x12\x14\n\x0c\x62\x63u_chrg_sts\x18\x05 \x01(\r\x12\x17\n\x0fobc_ac_chrg_mod\x18\x06 \x01(\r\x12\x15\n\rmessage_valid\x18\x07 \x01(\rb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chrgctrl_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CHRGCTRL._serialized_start=34
  _CHRGCTRL._serialized_end=224
  _CHRGTIPINFO._serialized_start=227
  _CHRGTIPINFO._serialized_end=420
  _OBCCHRGINPOUTP._serialized_start=423
  _OBCCHRGINPOUTP._serialized_end=708
  _CHRGCTRLSTS._serialized_start=711
  _CHRGCTRLSTS._serialized_end=892
# @@protoc_insertion_point(module_scope)
