# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hmi_ad_funset.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13hmi_ad_funset.proto\x12\x0cHmiInterface\"\x82\x05\n\x0eHmiADCruiseset\x12\x15\n\rad_curisemode\x18\x01 \x01(\r\x12\x1a\n\x12\x61\x64_idaenablestatus\x18\x02 \x01(\r\x12\x14\n\x0c\x61\x64_idastatus\x18\x03 \x01(\r\x12\x1e\n\x16\x61\x64_lanechangefrequency\x18\x04 \x01(\r\x12\x1b\n\x13\x61\x64_udlcenablestatus\x18\x05 \x01(\r\x12\x1b\n\x13\x61\x64_nidaudiowarstyle\x18\x06 \x01(\r\x12\x1b\n\x13\x61\x64_cslaenablestatus\x18\x07 \x01(\r\x12\x18\n\x10\x61\x64_cslmodestatus\x18\x08 \x01(\r\x12$\n\x1c\x61\x64_overspeedsoundwarningenst\x18\t \x01(\r\x12\x1a\n\x12\x61\x64_cslwarnoffsettp\x18\n \x01(\r\x12\x1f\n\x17\x61\x64_absoverspdwarnoffset\x18\x0b \x01(\r\x12\x1f\n\x17\x61\x64_reloverspdwarnoffset\x18\x0c \x01(\r\x12\x19\n\x11\x61\x64_autodrivestyle\x18\r \x01(\r\x12\x15\n\rad_adaccstyle\x18\x0e \x01(\r\x12\x17\n\x0f\x61\x64_adstartstyle\x18\x0f \x01(\r\x12\x17\n\x0f\x61\x64_adcurvestyle\x18\x10 \x01(\r\x12\x1c\n\x14\x61\x64_adlanechangestyle\x18\x11 \x01(\r\x12#\n\x1b\x61\x64_vehiclestartremindenable\x18\x12 \x01(\r\x12\x1a\n\x12\x61\x64_rcwenablestatus\x18\x13 \x01(\r\x12\x18\n\x10\x61\x64_seamodestatus\x18\x14 \x01(\r\x12\x18\n\x10\x61\x64_bsdlcasetting\x18\x15 \x01(\r\x12\x1b\n\x13\x61\x64_bsdlcaremindmode\x18\x16 \x01(\r\"g\n\x0cHmiADParkSet\x12\x1f\n\x17\x61\x64_amenityparkingenable\x18\x01 \x01(\r\x12\x16\n\x0e\x61\x64_parkingform\x18\x02 \x01(\r\x12\x1e\n\x16\x61\x64_memeryparkingenable\x18\x03 \x01(\r\"0\n\x12\x41PASetSpeedtypeSet\x12\x1a\n\x12\x61\x64_apasetspeedtype\x18\x01 \x01(\r\",\n\x10\x41utoParkStyleSet\x12\x18\n\x10\x61\x64_autoparkstyle\x18\x01 \x01(\r\"8\n\x16IACCFamlrRdModSwtFbSet\x12\x1e\n\x16\x63\x32_iaccfamlrrdmodswtfb\x18\x01 \x01(\r\")\n\rADScoreStsSet\x12\x18\n\x10\x63\x32_adscorestsset\x18\x01 \x01(\r\"\x96\x02\n\x10HmiADASSecureSet\x12\x14\n\x0c\x61\x64_elkenable\x18\x01 \x01(\r\x12\x14\n\x0c\x61\x64_cecenable\x18\x02 \x01(\r\x12!\n\x19\x61\x64_lasmodeselectionstatus\x18\x03 \x01(\r\x12+\n#ad_lasintellgentmodeselectionstatus\x18\x04 \x01(\r\x12%\n\x1d\x61\x64_laswarningmodeselectionsts\x18\x05 \x01(\r\x12\x1e\n\x16\x61\x64_forwardcolliasttype\x18\x06 \x01(\r\x12\"\n\x1a\x61\x64_forwardcolliastsenstyle\x18\x07 \x01(\r\x12\x1b\n\x13\x61\x64_rearcolliasttype\x18\x08 \x01(\r\"2\n\x0fRedLightReEnSet\x12\x1f\n\x17\x61\x64_redlightremindenable\x18\x01 \x01(\r\"+\n\rDiagnosisInfo\x12\x1a\n\x12heart_beat_counter\x18\x01 \x01(\r\"*\n\x11\x41\x63\x63PedalForSetMsg\x12\x15\n\rpedalforeable\x18\x01 \x01(\r\"*\n\x11\x41\x63\x63PedalAftSetMsg\x12\x15\n\rpedalafteable\x18\x01 \x01(\r\"F\n\x12\x41\x63\x63PedalStsChagMsg\x12\x17\n\x0f\x61\x63\x63pedalformode\x18\x01 \x01(\r\x12\x17\n\x0f\x61\x63\x63pedalaftmode\x18\x02 \x01(\r\"\x7f\n\x0c\x41\x44\x41SvoiceCtr\x12\x1a\n\x12voicelanechangereq\x18\x01 \x01(\r\x12\x16\n\x0evoiceaccactive\x18\x02 \x01(\r\x12\x1e\n\x16voicecruisesetdistance\x18\x03 \x01(\r\x12\x1b\n\x13voicecruisesetspeed\x18\x04 \x01(\r\")\n\rNIDSelfLrngFb\x12\x18\n\x10\x61\x64_nidselflrngfb\x18\x01 \x01(\r\"(\n\x0e\x42SDLCAOnOffSet\x12\x16\n\x0e\x61\x64_bsdlcaonoff\x18\x01 \x01(\r\"%\n\x0bSEAOnOffSts\x12\x16\n\x0e\x61\x64_seaonoffsts\x18\x01 \x01(\r\"\x93\x07\n\x0bHmiADFunset\x12\x36\n\x10hmi_ad_cruiseset\x18\x01 \x01(\x0b\x32\x1c.HmiInterface.HmiADCruiseset\x12\x31\n\x0c\x61\x64_score_set\x18\x02 \x01(\x0b\x32\x1b.HmiInterface.ADScoreStsSet\x12\x44\n\x16iacc_famlrrdmodswt_set\x18\x03 \x01(\x0b\x32$.HmiInterface.IACCFamlrRdModSwtFbSet\x12\x36\n\x0ehmi_secure_set\x18\x04 \x01(\x0b\x32\x1e.HmiInterface.HmiADASSecureSet\x12<\n\x12\x61pa_set_speed_type\x18\x05 \x01(\x0b\x32 .HmiInterface.APASetSpeedtypeSet\x12\x37\n\x0f\x61uto_park_style\x18\x06 \x01(\x0b\x32\x1e.HmiInterface.AutoParkStyleSet\x12\x32\n\x0ehmi_ad_parkset\x18\x07 \x01(\x0b\x32\x1a.HmiInterface.HmiADParkSet\x12=\n\x16hmi_ad_redlightreenset\x18\x08 \x01(\x0b\x32\x1d.HmiInterface.RedLightReEnSet\x12\x41\n\x18hmi_ad_accpedalforsetmsg\x18\t \x01(\x0b\x32\x1f.HmiInterface.AccPedalForSetMsg\x12\x41\n\x18hmi_ad_accpedalaftsetmsg\x18\n \x01(\x0b\x32\x1f.HmiInterface.AccPedalAftSetMsg\x12\x43\n\x19hmi_ad_accpedalstschagmsg\x18\x0b \x01(\x0b\x32 .HmiInterface.AccPedalStsChagMsg\x12\x37\n\x13hmi_hu_adasvoicectr\x18\x0c \x01(\x0b\x32\x1a.HmiInterface.ADASvoiceCtr\x12\x39\n\x14hmi_hu_nidselflrngfb\x18\r \x01(\x0b\x32\x1b.HmiInterface.NIDSelfLrngFb\x12;\n\x15hmi_hu_bsdlcaonoffset\x18\x0e \x01(\x0b\x32\x1c.HmiInterface.BSDLCAOnOffSet\x12\x35\n\x12hmi_hu_seaonoffsts\x18\x0f \x01(\x0b\x32\x19.HmiInterface.SEAOnOffStsb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'hmi_ad_funset_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HMIADCRUISESET._serialized_start=38
  _HMIADCRUISESET._serialized_end=680
  _HMIADPARKSET._serialized_start=682
  _HMIADPARKSET._serialized_end=785
  _APASETSPEEDTYPESET._serialized_start=787
  _APASETSPEEDTYPESET._serialized_end=835
  _AUTOPARKSTYLESET._serialized_start=837
  _AUTOPARKSTYLESET._serialized_end=881
  _IACCFAMLRRDMODSWTFBSET._serialized_start=883
  _IACCFAMLRRDMODSWTFBSET._serialized_end=939
  _ADSCORESTSSET._serialized_start=941
  _ADSCORESTSSET._serialized_end=982
  _HMIADASSECURESET._serialized_start=985
  _HMIADASSECURESET._serialized_end=1263
  _REDLIGHTREENSET._serialized_start=1265
  _REDLIGHTREENSET._serialized_end=1315
  _DIAGNOSISINFO._serialized_start=1317
  _DIAGNOSISINFO._serialized_end=1360
  _ACCPEDALFORSETMSG._serialized_start=1362
  _ACCPEDALFORSETMSG._serialized_end=1404
  _ACCPEDALAFTSETMSG._serialized_start=1406
  _ACCPEDALAFTSETMSG._serialized_end=1448
  _ACCPEDALSTSCHAGMSG._serialized_start=1450
  _ACCPEDALSTSCHAGMSG._serialized_end=1520
  _ADASVOICECTR._serialized_start=1522
  _ADASVOICECTR._serialized_end=1649
  _NIDSELFLRNGFB._serialized_start=1651
  _NIDSELFLRNGFB._serialized_end=1692
  _BSDLCAONOFFSET._serialized_start=1694
  _BSDLCAONOFFSET._serialized_end=1734
  _SEAONOFFSTS._serialized_start=1736
  _SEAONOFFSTS._serialized_end=1773
  _HMIADFUNSET._serialized_start=1776
  _HMIADFUNSET._serialized_end=2691
# @@protoc_insertion_point(module_scope)
