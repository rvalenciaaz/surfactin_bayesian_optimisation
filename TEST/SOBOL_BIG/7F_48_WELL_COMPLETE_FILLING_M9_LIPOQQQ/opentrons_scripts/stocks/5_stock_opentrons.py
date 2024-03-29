from opentrons import protocol_api
metadata = {'apiLevel': '2.13'}
def run(protocol: protocol_api.ProtocolContext):
	tiprack_1 = protocol.load_labware('opentrons_96_tiprack_1000ul',10)
	tiprack_2 = protocol.load_labware('opentrons_96_tiprack_300ul', 11)
	reservoir_1= protocol.load_labware('opentrons_24_tuberack_eppendorf_2ml_safelock_snapcap',1)
	reservoir_2= protocol.load_labware('opentrons_24_tuberack_eppendorf_2ml_safelock_snapcap',2)
	reservoir_3= protocol.load_labware('opentrons_24_tuberack_eppendorf_2ml_safelock_snapcap',3)
	reservoir_4= protocol.load_labware('opentrons_24_tuberack_eppendorf_2ml_safelock_snapcap',4)
	big1=protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical',6)
	big2=protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical',9)
	p1000 = protocol.load_instrument('p1000_single', 'right', tip_racks=[tiprack_1])
	p300 = protocol.load_instrument('p300_single', 'left', tip_racks=[tiprack_2])
	#Vol_Glucose
	p300.pick_up_tip()
	p1000.pick_up_tip()
	p1000.aspirate(667.4,big1['A3'],rate=0.7)
	p1000.dispense(667.4,reservoir_1['A1'],rate=0.7)
	p1000.aspirate(610.25,big1['A3'],rate=0.7)
	p1000.dispense(610.25,reservoir_1['A2'],rate=0.7)
	p1000.aspirate(610.25,big1['A3'],rate=0.7)
	p1000.dispense(610.25,reservoir_1['A2'],rate=0.7)
	p1000.aspirate(521.80,big1['A3'],rate=0.7)
	p1000.dispense(521.80,reservoir_1['A3'],rate=0.7)
	p1000.aspirate(521.80,big1['A3'],rate=0.7)
	p1000.dispense(521.80,reservoir_1['A3'],rate=0.7)
	p300.aspirate(222.7,big1['A3'],rate=0.7)
	p300.dispense(222.7,reservoir_1['A4'],rate=0.7)
	p1000.aspirate(569.65,big1['A3'],rate=0.7)
	p1000.dispense(569.65,reservoir_1['A5'],rate=0.7)
	p1000.aspirate(569.65,big1['A3'],rate=0.7)
	p1000.dispense(569.65,reservoir_1['A5'],rate=0.7)
	p1000.aspirate(477.1,big1['A3'],rate=0.7)
	p1000.dispense(477.1,reservoir_1['A6'],rate=0.7)
	p1000.aspirate(939.20,big1['A3'],rate=0.7)
	p1000.dispense(939.20,reservoir_1['B1'],rate=0.7)
	p1000.aspirate(939.20,big1['A3'],rate=0.7)
	p1000.dispense(939.20,reservoir_1['B1'],rate=0.7)
	p300.aspirate(200.0,big1['A3'],rate=0.7)
	p300.dispense(200.0,reservoir_1['B2'],rate=0.7)
	p300.aspirate(200.0,big1['A3'],rate=0.7)
	p300.dispense(200.0,reservoir_1['B3'],rate=0.7)
	p300.drop_tip()
	p1000.drop_tip()
	#Water_Glucose
	p300.pick_up_tip()
	p1000.pick_up_tip()
	p1000.aspirate(666.30,big2['B4'],rate=0.7)
	p1000.dispense(666.30,reservoir_1['A1'],rate=0.7)
	p1000.aspirate(666.30,big2['B4'],rate=0.7)
	p1000.dispense(666.30,reservoir_1['A1'],rate=0.7)
	p1000.aspirate(779.5,big2['B4'],rate=0.7)
	p1000.dispense(779.5,reservoir_1['A2'],rate=0.7)
	p1000.aspirate(956.4,big2['B4'],rate=0.7)
	p1000.dispense(956.4,reservoir_1['A3'],rate=0.7)
	p1000.aspirate(888.65,big2['B4'],rate=0.7)
	p1000.dispense(888.65,reservoir_1['A4'],rate=0.7)
	p1000.aspirate(888.65,big2['B4'],rate=0.7)
	p1000.dispense(888.65,reservoir_1['A4'],rate=0.7)
	p1000.aspirate(860.7,big2['B4'],rate=0.7)
	p1000.dispense(860.7,reservoir_1['A5'],rate=0.7)
	p1000.aspirate(761.45,big2['B4'],rate=0.7)
	p1000.dispense(761.45,reservoir_1['A6'],rate=0.7)
	p1000.aspirate(761.45,big2['B4'],rate=0.7)
	p1000.dispense(761.45,reservoir_1['A6'],rate=0.7)
	p300.aspirate(121.6,big2['B4'],rate=0.7)
	p300.dispense(121.6,reservoir_1['B1'],rate=0.7)
	p1000.aspirate(900.00,big2['B4'],rate=0.7)
	p1000.dispense(900.00,reservoir_1['B2'],rate=0.7)
	p1000.aspirate(900.00,big2['B4'],rate=0.7)
	p1000.dispense(900.00,reservoir_1['B2'],rate=0.7)
	p1000.aspirate(900.00,big2['B4'],rate=0.7)
	p1000.dispense(900.00,reservoir_1['B3'],rate=0.7)
	p1000.aspirate(900.00,big2['B4'],rate=0.7)
	p1000.dispense(900.00,reservoir_1['B3'],rate=0.7)
	p300.drop_tip()
	p1000.drop_tip()
	#Vol_NH4Cl
	p300.pick_up_tip()
	p1000.pick_up_tip()
	p300.aspirate(271.0,big1['A4'],rate=0.7)
	p300.dispense(271.0,reservoir_1['C1'],rate=0.7)
	p300.aspirate(189.5,big1['A4'],rate=0.7)
	p300.dispense(189.5,reservoir_1['C2'],rate=0.7)
	p1000.aspirate(760.80,big1['A4'],rate=0.7)
	p1000.dispense(760.80,reservoir_1['C3'],rate=0.7)
	p1000.aspirate(760.80,big1['A4'],rate=0.7)
	p1000.dispense(760.80,reservoir_1['C3'],rate=0.7)
	p1000.aspirate(500.80,big1['A4'],rate=0.7)
	p1000.dispense(500.80,reservoir_1['C4'],rate=0.7)
	p1000.aspirate(500.80,big1['A4'],rate=0.7)
	p1000.dispense(500.80,reservoir_1['C4'],rate=0.7)
	p1000.aspirate(614.25,big1['A4'],rate=0.7)
	p1000.dispense(614.25,reservoir_1['C5'],rate=0.7)
	p1000.aspirate(614.25,big1['A4'],rate=0.7)
	p1000.dispense(614.25,reservoir_1['C5'],rate=0.7)
	p1000.aspirate(909.60,big1['A4'],rate=0.7)
	p1000.dispense(909.60,reservoir_1['C6'],rate=0.7)
	p1000.aspirate(909.60,big1['A4'],rate=0.7)
	p1000.dispense(909.60,reservoir_1['C6'],rate=0.7)
	p300.aspirate(284.3,big1['A4'],rate=0.7)
	p300.dispense(284.3,reservoir_1['D1'],rate=0.7)
	p300.aspirate(155.8,big1['A4'],rate=0.7)
	p300.dispense(155.8,reservoir_1['D2'],rate=0.7)
	p300.aspirate(155.8,big1['A4'],rate=0.7)
	p300.dispense(155.8,reservoir_1['D3'],rate=0.7)
	p300.drop_tip()
	p1000.drop_tip()
	#Water_NH4Cl
	p300.pick_up_tip()
	p1000.pick_up_tip()
	p1000.aspirate(864.50,big2['B4'],rate=0.7)
	p1000.dispense(864.50,reservoir_1['C1'],rate=0.7)
	p1000.aspirate(864.50,big2['B4'],rate=0.7)
	p1000.dispense(864.50,reservoir_1['C1'],rate=0.7)
	p1000.aspirate(905.25,big2['B4'],rate=0.7)
	p1000.dispense(905.25,reservoir_1['C2'],rate=0.7)
	p1000.aspirate(905.25,big2['B4'],rate=0.7)
	p1000.dispense(905.25,reservoir_1['C2'],rate=0.7)
	p1000.aspirate(478.4,big2['B4'],rate=0.7)
	p1000.dispense(478.4,reservoir_1['C3'],rate=0.7)
	p1000.aspirate(998.4,big2['B4'],rate=0.7)
	p1000.dispense(998.4,reservoir_1['C4'],rate=0.7)
	p1000.aspirate(771.5,big2['B4'],rate=0.7)
	p1000.dispense(771.5,reservoir_1['C5'],rate=0.7)
	p300.aspirate(180.8,big2['B4'],rate=0.7)
	p300.dispense(180.8,reservoir_1['C6'],rate=0.7)
	p1000.aspirate(857.85,big2['B4'],rate=0.7)
	p1000.dispense(857.85,reservoir_1['D1'],rate=0.7)
	p1000.aspirate(857.85,big2['B4'],rate=0.7)
	p1000.dispense(857.85,reservoir_1['D1'],rate=0.7)
	p1000.aspirate(922.10,big2['B4'],rate=0.7)
	p1000.dispense(922.10,reservoir_1['D2'],rate=0.7)
	p1000.aspirate(922.10,big2['B4'],rate=0.7)
	p1000.dispense(922.10,reservoir_1['D2'],rate=0.7)
	p1000.aspirate(922.10,big2['B4'],rate=0.7)
	p1000.dispense(922.10,reservoir_1['D3'],rate=0.7)
	p1000.aspirate(922.10,big2['B4'],rate=0.7)
	p1000.dispense(922.10,reservoir_1['D3'],rate=0.7)
	p300.drop_tip()
	p1000.drop_tip()
	#Vol_MgSO4
	p300.pick_up_tip()
	p1000.pick_up_tip()
	p300.aspirate(282.9,big1['B3'],rate=0.7)
	p300.dispense(282.9,reservoir_2['A1'],rate=0.7)
	p1000.aspirate(669.05,big1['B3'],rate=0.7)
	p1000.dispense(669.05,reservoir_2['A2'],rate=0.7)
	p1000.aspirate(669.05,big1['B3'],rate=0.7)
	p1000.dispense(669.05,reservoir_2['A2'],rate=0.7)
	p1000.aspirate(983.7,big1['B3'],rate=0.7)
	p1000.dispense(983.7,reservoir_2['A3'],rate=0.7)
	p1000.aspirate(835.35,big1['B3'],rate=0.7)
	p1000.dispense(835.35,reservoir_2['A4'],rate=0.7)
	p1000.aspirate(835.35,big1['B3'],rate=0.7)
	p1000.dispense(835.35,reservoir_2['A4'],rate=0.7)
	p1000.aspirate(362.2,big1['B3'],rate=0.7)
	p1000.dispense(362.2,reservoir_2['A5'],rate=0.7)
	p1000.aspirate(547.9,big1['B3'],rate=0.7)
	p1000.dispense(547.9,reservoir_2['A6'],rate=0.7)
	p1000.aspirate(701.65,big1['B3'],rate=0.7)
	p1000.dispense(701.65,reservoir_2['B1'],rate=0.7)
	p1000.aspirate(701.65,big1['B3'],rate=0.7)
	p1000.dispense(701.65,reservoir_2['B1'],rate=0.7)
	p1000.aspirate(1000.00,big1['B3'],rate=0.7)
	p1000.dispense(1000.00,reservoir_2['B2'],rate=0.7)
	p1000.aspirate(1000.00,big1['B3'],rate=0.7)
	p1000.dispense(1000.00,reservoir_2['B2'],rate=0.7)
	p1000.aspirate(1000.00,big1['B3'],rate=0.7)
	p1000.dispense(1000.00,reservoir_2['B3'],rate=0.7)
	p1000.aspirate(1000.00,big1['B3'],rate=0.7)
	p1000.dispense(1000.00,reservoir_2['B3'],rate=0.7)
	p300.drop_tip()
	p1000.drop_tip()
	#Water_MgSO4
	p300.pick_up_tip()
	p1000.pick_up_tip()
	p1000.aspirate(858.55,big2['B4'],rate=0.7)
	p1000.dispense(858.55,reservoir_2['A1'],rate=0.7)
	p1000.aspirate(858.55,big2['B4'],rate=0.7)
	p1000.dispense(858.55,reservoir_2['A1'],rate=0.7)
	p1000.aspirate(661.9,big2['B4'],rate=0.7)
	p1000.dispense(661.9,reservoir_2['A2'],rate=0.7)
	p1000.aspirate(508.15,big2['B4'],rate=0.7)
	p1000.dispense(508.15,reservoir_2['A3'],rate=0.7)
	p1000.aspirate(508.15,big2['B4'],rate=0.7)
	p1000.dispense(508.15,reservoir_2['A3'],rate=0.7)
	p1000.aspirate(329.3,big2['B4'],rate=0.7)
	p1000.dispense(329.3,reservoir_2['A4'],rate=0.7)
	p1000.aspirate(818.90,big2['B4'],rate=0.7)
	p1000.dispense(818.90,reservoir_2['A5'],rate=0.7)
	p1000.aspirate(818.90,big2['B4'],rate=0.7)
	p1000.dispense(818.90,reservoir_2['A5'],rate=0.7)
	p1000.aspirate(726.05,big2['B4'],rate=0.7)
	p1000.dispense(726.05,reservoir_2['A6'],rate=0.7)
	p1000.aspirate(726.05,big2['B4'],rate=0.7)
	p1000.dispense(726.05,reservoir_2['A6'],rate=0.7)
	p1000.aspirate(596.7,big2['B4'],rate=0.7)
	p1000.dispense(596.7,reservoir_2['B1'],rate=0.7)
	p300.drop_tip()
	p1000.drop_tip()
	#Vol_KH2PO4
	p1000.pick_up_tip()
	p1000.aspirate(320.9,big1['B4'],rate=0.7)
	p1000.dispense(320.9,reservoir_2['C1'],rate=0.7)
	p1000.aspirate(701.70,big1['B4'],rate=0.7)
	p1000.dispense(701.70,reservoir_2['C2'],rate=0.7)
	p1000.aspirate(701.70,big1['B4'],rate=0.7)
	p1000.dispense(701.70,reservoir_2['C2'],rate=0.7)
	p1000.aspirate(965.80,big1['B4'],rate=0.7)
	p1000.dispense(965.80,reservoir_2['C3'],rate=0.7)
	p1000.aspirate(965.80,big1['B4'],rate=0.7)
	p1000.dispense(965.80,reservoir_2['C3'],rate=0.7)
	p1000.aspirate(697.9,big1['B4'],rate=0.7)
	p1000.dispense(697.9,reservoir_2['C4'],rate=0.7)
	p1000.aspirate(797.3,big1['B4'],rate=0.7)
	p1000.dispense(797.3,reservoir_2['C5'],rate=0.7)
	p1000.aspirate(438.5,big1['B4'],rate=0.7)
	p1000.dispense(438.5,reservoir_2['C6'],rate=0.7)
	p1000.aspirate(766.25,big1['B4'],rate=0.7)
	p1000.dispense(766.25,reservoir_2['D1'],rate=0.7)
	p1000.aspirate(766.25,big1['B4'],rate=0.7)
	p1000.dispense(766.25,reservoir_2['D1'],rate=0.7)
	p1000.aspirate(881.6,big1['B4'],rate=0.7)
	p1000.dispense(881.6,reservoir_2['D2'],rate=0.7)
	p1000.aspirate(881.6,big1['B4'],rate=0.7)
	p1000.dispense(881.6,reservoir_2['D3'],rate=0.7)
	p1000.drop_tip()
	#Water_KH2PO4
	p300.pick_up_tip()
	p1000.pick_up_tip()
	p1000.aspirate(839.55,big2['B4'],rate=0.7)
	p1000.dispense(839.55,reservoir_2['C1'],rate=0.7)
	p1000.aspirate(839.55,big2['B4'],rate=0.7)
	p1000.dispense(839.55,reservoir_2['C1'],rate=0.7)
	p1000.aspirate(596.6,big2['B4'],rate=0.7)
	p1000.dispense(596.6,reservoir_2['C2'],rate=0.7)
	p300.aspirate(68.4,big2['B4'],rate=0.7)
	p300.dispense(68.4,reservoir_2['C3'],rate=0.7)
	p1000.aspirate(651.05,big2['B4'],rate=0.7)
	p1000.dispense(651.05,reservoir_2['C4'],rate=0.7)
	p1000.aspirate(651.05,big2['B4'],rate=0.7)
	p1000.dispense(651.05,reservoir_2['C4'],rate=0.7)
	p1000.aspirate(601.35,big2['B4'],rate=0.7)
	p1000.dispense(601.35,reservoir_2['C5'],rate=0.7)
	p1000.aspirate(601.35,big2['B4'],rate=0.7)
	p1000.dispense(601.35,reservoir_2['C5'],rate=0.7)
	p1000.aspirate(780.75,big2['B4'],rate=0.7)
	p1000.dispense(780.75,reservoir_2['C6'],rate=0.7)
	p1000.aspirate(780.75,big2['B4'],rate=0.7)
	p1000.dispense(780.75,reservoir_2['C6'],rate=0.7)
	p1000.aspirate(467.5,big2['B4'],rate=0.7)
	p1000.dispense(467.5,reservoir_2['D1'],rate=0.7)
	p1000.aspirate(559.20,big2['B4'],rate=0.7)
	p1000.dispense(559.20,reservoir_2['D2'],rate=0.7)
	p1000.aspirate(559.20,big2['B4'],rate=0.7)
	p1000.dispense(559.20,reservoir_2['D2'],rate=0.7)
	p1000.aspirate(559.20,big2['B4'],rate=0.7)
	p1000.dispense(559.20,reservoir_2['D3'],rate=0.7)
	p1000.aspirate(559.20,big2['B4'],rate=0.7)
	p1000.dispense(559.20,reservoir_2['D3'],rate=0.7)
	p300.drop_tip()
	p1000.drop_tip()
	#Vol_Na2HPO4
	p300.pick_up_tip()
	p1000.pick_up_tip()
	p1000.aspirate(965.75,big2['A3'],rate=0.7)
	p1000.dispense(965.75,reservoir_3['A1'],rate=0.7)
	p1000.aspirate(965.75,big2['A3'],rate=0.7)
	p1000.dispense(965.75,reservoir_3['A1'],rate=0.7)
	p300.aspirate(78.8,big2['A3'],rate=0.7)
	p300.dispense(78.8,reservoir_3['A2'],rate=0.7)
	p1000.aspirate(885.25,big2['A3'],rate=0.7)
	p1000.dispense(885.25,reservoir_3['A3'],rate=0.7)
	p1000.aspirate(885.25,big2['A3'],rate=0.7)
	p1000.dispense(885.25,reservoir_3['A3'],rate=0.7)
	p1000.aspirate(986.05,big2['A3'],rate=0.7)
	p1000.dispense(986.05,reservoir_3['A4'],rate=0.7)
	p1000.aspirate(986.05,big2['A3'],rate=0.7)
	p1000.dispense(986.05,reservoir_3['A4'],rate=0.7)
	p1000.aspirate(511.70,big2['A3'],rate=0.7)
	p1000.dispense(511.70,reservoir_3['A5'],rate=0.7)
	p1000.aspirate(511.70,big2['A3'],rate=0.7)
	p1000.dispense(511.70,reservoir_3['A5'],rate=0.7)
	p1000.aspirate(304.2,big2['A3'],rate=0.7)
	p1000.dispense(304.2,reservoir_3['A6'],rate=0.7)
	p1000.aspirate(799.1,big2['A3'],rate=0.7)
	p1000.dispense(799.1,reservoir_3['B1'],rate=0.7)
	p1000.aspirate(845.20,big2['A3'],rate=0.7)
	p1000.dispense(845.20,reservoir_3['B2'],rate=0.7)
	p1000.aspirate(845.20,big2['A3'],rate=0.7)
	p1000.dispense(845.20,reservoir_3['B2'],rate=0.7)
	p1000.aspirate(845.20,big2['A3'],rate=0.7)
	p1000.dispense(845.20,reservoir_3['B3'],rate=0.7)
	p1000.aspirate(845.20,big2['A3'],rate=0.7)
	p1000.dispense(845.20,reservoir_3['B3'],rate=0.7)
	p300.drop_tip()
	p1000.drop_tip()
	#Water_Na2HPO4
	p300.pick_up_tip()
	p1000.pick_up_tip()
	p300.aspirate(68.5,big2['B4'],rate=0.7)
	p300.dispense(68.5,reservoir_3['A1'],rate=0.7)
	p1000.aspirate(960.60,big2['B4'],rate=0.7)
	p1000.dispense(960.60,reservoir_3['A2'],rate=0.7)
	p1000.aspirate(960.60,big2['B4'],rate=0.7)
	p1000.dispense(960.60,reservoir_3['A2'],rate=0.7)
	p300.aspirate(229.5,big2['B4'],rate=0.7)
	p300.dispense(229.5,reservoir_3['A3'],rate=0.7)
	p300.aspirate(27.9,big2['B4'],rate=0.7)
	p300.dispense(27.9,reservoir_3['A4'],rate=0.7)
	p1000.aspirate(976.6,big2['B4'],rate=0.7)
	p1000.dispense(976.6,reservoir_3['A5'],rate=0.7)
	p1000.aspirate(847.90,big2['B4'],rate=0.7)
	p1000.dispense(847.90,reservoir_3['A6'],rate=0.7)
	p1000.aspirate(847.90,big2['B4'],rate=0.7)
	p1000.dispense(847.90,reservoir_3['A6'],rate=0.7)
	p1000.aspirate(600.45,big2['B4'],rate=0.7)
	p1000.dispense(600.45,reservoir_3['B1'],rate=0.7)
	p1000.aspirate(600.45,big2['B4'],rate=0.7)
	p1000.dispense(600.45,reservoir_3['B1'],rate=0.7)
	p1000.aspirate(309.6,big2['B4'],rate=0.7)
	p1000.dispense(309.6,reservoir_3['B2'],rate=0.7)
	p1000.aspirate(309.6,big2['B4'],rate=0.7)
	p1000.dispense(309.6,reservoir_3['B3'],rate=0.7)
	p300.drop_tip()
	p1000.drop_tip()
	#Vol_CaCl2
	p300.pick_up_tip()
	p1000.pick_up_tip()
	p1000.aspirate(859.40,big2['A4'],rate=0.7)
	p1000.dispense(859.40,reservoir_3['C1'],rate=0.7)
	p1000.aspirate(859.40,big2['A4'],rate=0.7)
	p1000.dispense(859.40,reservoir_3['C1'],rate=0.7)
	p1000.aspirate(878.1,big2['A4'],rate=0.7)
	p1000.dispense(878.1,reservoir_3['C2'],rate=0.7)
	p1000.aspirate(711.8,big2['A4'],rate=0.7)
	p1000.dispense(711.8,reservoir_3['C3'],rate=0.7)
	p300.aspirate(16.4,big2['A4'],rate=0.7)
	p300.dispense(16.4,reservoir_3['C4'],rate=0.7)
	p1000.aspirate(882.85,big2['A4'],rate=0.7)
	p1000.dispense(882.85,reservoir_3['C5'],rate=0.7)
	p1000.aspirate(882.85,big2['A4'],rate=0.7)
	p1000.dispense(882.85,reservoir_3['C5'],rate=0.7)
	p1000.aspirate(981.0,big2['A4'],rate=0.7)
	p1000.dispense(981.0,reservoir_3['C6'],rate=0.7)
	p1000.aspirate(905.10,big2['A4'],rate=0.7)
	p1000.dispense(905.10,reservoir_3['D1'],rate=0.7)
	p1000.aspirate(905.10,big2['A4'],rate=0.7)
	p1000.dispense(905.10,reservoir_3['D1'],rate=0.7)
	p1000.aspirate(1000.0,big2['A4'],rate=0.7)
	p1000.dispense(1000.0,reservoir_3['D2'],rate=0.7)
	p1000.aspirate(1000.0,big2['A4'],rate=0.7)
	p1000.dispense(1000.0,reservoir_3['D3'],rate=0.7)
	p300.drop_tip()
	p1000.drop_tip()
	#Water_CaCl2
	p300.pick_up_tip()
	p1000.pick_up_tip()
	p300.aspirate(281.2,big2['B4'],rate=0.7)
	p300.dispense(281.2,reservoir_3['C1'],rate=0.7)
	p1000.aspirate(560.95,big2['B4'],rate=0.7)
	p1000.dispense(560.95,reservoir_3['C2'],rate=0.7)
	p1000.aspirate(560.95,big2['B4'],rate=0.7)
	p1000.dispense(560.95,reservoir_3['C2'],rate=0.7)
	p1000.aspirate(644.10,big2['B4'],rate=0.7)
	p1000.dispense(644.10,reservoir_3['C3'],rate=0.7)
	p1000.aspirate(644.10,big2['B4'],rate=0.7)
	p1000.dispense(644.10,reservoir_3['C3'],rate=0.7)
	p1000.aspirate(991.80,big2['B4'],rate=0.7)
	p1000.dispense(991.80,reservoir_3['C4'],rate=0.7)
	p1000.aspirate(991.80,big2['B4'],rate=0.7)
	p1000.dispense(991.80,reservoir_3['C4'],rate=0.7)
	p300.aspirate(234.3,big2['B4'],rate=0.7)
	p300.dispense(234.3,reservoir_3['C5'],rate=0.7)
	p1000.aspirate(509.50,big2['B4'],rate=0.7)
	p1000.dispense(509.50,reservoir_3['C6'],rate=0.7)
	p1000.aspirate(509.50,big2['B4'],rate=0.7)
	p1000.dispense(509.50,reservoir_3['C6'],rate=0.7)
	p300.aspirate(189.8,big2['B4'],rate=0.7)
	p300.dispense(189.8,reservoir_3['D1'],rate=0.7)
	p1000.aspirate(1000.0,big2['B4'],rate=0.7)
	p1000.dispense(1000.0,reservoir_3['D2'],rate=0.7)
	p1000.aspirate(1000.0,big2['B4'],rate=0.7)
	p1000.dispense(1000.0,reservoir_3['D3'],rate=0.7)
	p300.drop_tip()
	p1000.drop_tip()
	#Vol_NaCl
	p1000.pick_up_tip()
	p1000.aspirate(570.00,big2['B3'],rate=0.7)
	p1000.dispense(570.00,reservoir_4['A1'],rate=0.7)
	p1000.aspirate(570.00,big2['B3'],rate=0.7)
	p1000.dispense(570.00,reservoir_4['A1'],rate=0.7)
	p1000.aspirate(697.80,big2['B3'],rate=0.7)
	p1000.dispense(697.80,reservoir_4['A2'],rate=0.7)
	p1000.aspirate(697.80,big2['B3'],rate=0.7)
	p1000.dispense(697.80,reservoir_4['A2'],rate=0.7)
	p1000.aspirate(696.3,big2['B3'],rate=0.7)
	p1000.dispense(696.3,reservoir_4['A3'],rate=0.7)
	p1000.aspirate(755.20,big2['B3'],rate=0.7)
	p1000.dispense(755.20,reservoir_4['A4'],rate=0.7)
	p1000.aspirate(755.20,big2['B3'],rate=0.7)
	p1000.dispense(755.20,reservoir_4['A4'],rate=0.7)
	p1000.aspirate(975.70,big2['B3'],rate=0.7)
	p1000.dispense(975.70,reservoir_4['A5'],rate=0.7)
	p1000.aspirate(975.70,big2['B3'],rate=0.7)
	p1000.dispense(975.70,reservoir_4['A5'],rate=0.7)
	p1000.aspirate(644.80,big2['B3'],rate=0.7)
	p1000.dispense(644.80,reservoir_4['A6'],rate=0.7)
	p1000.aspirate(644.80,big2['B3'],rate=0.7)
	p1000.dispense(644.80,reservoir_4['A6'],rate=0.7)
	p1000.aspirate(431.0,big2['B3'],rate=0.7)
	p1000.dispense(431.0,reservoir_4['B1'],rate=0.7)
	p1000.aspirate(342.0,big2['B3'],rate=0.7)
	p1000.dispense(342.0,reservoir_4['B2'],rate=0.7)
	p1000.aspirate(342.0,big2['B3'],rate=0.7)
	p1000.dispense(342.0,reservoir_4['B3'],rate=0.7)
	p1000.drop_tip()
	#Water_NaCl
	p300.pick_up_tip()
	p1000.pick_up_tip()
	p1000.aspirate(860.0,big2['B4'],rate=0.7)
	p1000.dispense(860.0,reservoir_4['A1'],rate=0.7)
	p1000.aspirate(604.4,big2['B4'],rate=0.7)
	p1000.dispense(604.4,reservoir_4['A2'],rate=0.7)
	p1000.aspirate(651.85,big2['B4'],rate=0.7)
	p1000.dispense(651.85,reservoir_4['A3'],rate=0.7)
	p1000.aspirate(651.85,big2['B4'],rate=0.7)
	p1000.dispense(651.85,reservoir_4['A3'],rate=0.7)
	p1000.aspirate(489.6,big2['B4'],rate=0.7)
	p1000.dispense(489.6,reservoir_4['A4'],rate=0.7)
	p300.aspirate(48.6,big2['B4'],rate=0.7)
	p300.dispense(48.6,reservoir_4['A5'],rate=0.7)
	p1000.aspirate(710.4,big2['B4'],rate=0.7)
	p1000.dispense(710.4,reservoir_4['A6'],rate=0.7)
	p1000.aspirate(784.50,big2['B4'],rate=0.7)
	p1000.dispense(784.50,reservoir_4['B1'],rate=0.7)
	p1000.aspirate(784.50,big2['B4'],rate=0.7)
	p1000.dispense(784.50,reservoir_4['B1'],rate=0.7)
	p1000.aspirate(829.00,big2['B4'],rate=0.7)
	p1000.dispense(829.00,reservoir_4['B2'],rate=0.7)
	p1000.aspirate(829.00,big2['B4'],rate=0.7)
	p1000.dispense(829.00,reservoir_4['B2'],rate=0.7)
	p1000.aspirate(829.00,big2['B4'],rate=0.7)
	p1000.dispense(829.00,reservoir_4['B3'],rate=0.7)
	p1000.aspirate(829.00,big2['B4'],rate=0.7)
	p1000.dispense(829.00,reservoir_4['B3'],rate=0.7)
	p300.drop_tip()
	p1000.drop_tip()
