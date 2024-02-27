from opentrons import protocol_api
metadata = {'apiLevel': '2.13'}
def run(protocol: protocol_api.ProtocolContext):
	tiprack_1 = protocol.load_labware('opentrons_96_tiprack_1000ul',10)
	tiprack_2 = protocol.load_labware('opentrons_96_tiprack_300ul', 11)
	reservoir = protocol.load_labware('nest_96_wellplate_2ml_deep',5)
	big1=protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical',6)
	big2=protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical',9)
	p1000 = protocol.load_instrument('p1000_single', 'right', tip_racks=[tiprack_1])
	p300 = protocol.load_instrument('p300_single', 'left', tip_racks=[tiprack_2])
	#Vol_Glucose
	p300.pick_up_tip()
	p1000.pick_up_tip()
	p1000.aspirate(667.4,big1['A3'],rate=0.7)
	p1000.dispense(667.4,reservoir['A1'],rate=0.7)
	p1000.aspirate(644.40,big1['A3'],rate=0.7)
	p1000.dispense(644.40,reservoir['A2'],rate=0.7)
	p1000.aspirate(644.40,big1['A3'],rate=0.7)
	p1000.dispense(644.40,reservoir['A2'],rate=0.7)
	p1000.aspirate(975.25,big1['A3'],rate=0.7)
	p1000.dispense(975.25,reservoir['A3'],rate=0.7)
	p1000.aspirate(975.25,big1['A3'],rate=0.7)
	p1000.dispense(975.25,reservoir['A3'],rate=0.7)
	p300.aspirate(64.4,big1['A3'],rate=0.7)
	p300.dispense(64.4,reservoir['A4'],rate=0.7)
	p1000.aspirate(382.7,big1['A3'],rate=0.7)
	p1000.dispense(382.7,reservoir['A5'],rate=0.7)
	p1000.aspirate(755.50,big1['A3'],rate=0.7)
	p1000.dispense(755.50,reservoir['A6'],rate=0.7)
	p1000.aspirate(755.50,big1['A3'],rate=0.7)
	p1000.dispense(755.50,reservoir['A6'],rate=0.7)
	p1000.aspirate(610.25,big1['A3'],rate=0.7)
	p1000.dispense(610.25,reservoir['A7'],rate=0.7)
	p1000.aspirate(610.25,big1['A3'],rate=0.7)
	p1000.dispense(610.25,reservoir['A7'],rate=0.7)
	p300.aspirate(200.0,big1['A3'],rate=0.7)
	p300.dispense(200.0,reservoir['A8'],rate=0.7)
	p300.aspirate(200.0,big1['A3'],rate=0.7)
	p300.dispense(200.0,reservoir['A9'],rate=0.7)
	p300.drop_tip()
	p1000.drop_tip()
	#Water_Glucose
	p300.pick_up_tip()
	p1000.pick_up_tip()
	p1000.aspirate(666.30,big2['B4'],rate=0.7)
	p1000.dispense(666.30,reservoir['A1'],rate=0.7)
	p1000.aspirate(666.30,big2['B4'],rate=0.7)
	p1000.dispense(666.30,reservoir['A1'],rate=0.7)
	p1000.aspirate(711.2,big2['B4'],rate=0.7)
	p1000.dispense(711.2,reservoir['A2'],rate=0.7)
	p300.aspirate(49.5,big2['B4'],rate=0.7)
	p300.dispense(49.5,reservoir['A3'],rate=0.7)
	p1000.aspirate(967.80,big2['B4'],rate=0.7)
	p1000.dispense(967.80,reservoir['A4'],rate=0.7)
	p1000.aspirate(967.80,big2['B4'],rate=0.7)
	p1000.dispense(967.80,reservoir['A4'],rate=0.7)
	p1000.aspirate(808.65,big2['B4'],rate=0.7)
	p1000.dispense(808.65,reservoir['A5'],rate=0.7)
	p1000.aspirate(808.65,big2['B4'],rate=0.7)
	p1000.dispense(808.65,reservoir['A5'],rate=0.7)
	p1000.aspirate(489.0,big2['B4'],rate=0.7)
	p1000.dispense(489.0,reservoir['A6'],rate=0.7)
	p1000.aspirate(779.5,big2['B4'],rate=0.7)
	p1000.dispense(779.5,reservoir['A7'],rate=0.7)
	p1000.aspirate(900.00,big2['B4'],rate=0.7)
	p1000.dispense(900.00,reservoir['A8'],rate=0.7)
	p1000.aspirate(900.00,big2['B4'],rate=0.7)
	p1000.dispense(900.00,reservoir['A8'],rate=0.7)
	p1000.aspirate(900.00,big2['B4'],rate=0.7)
	p1000.dispense(900.00,reservoir['A9'],rate=0.7)
	p1000.aspirate(900.00,big2['B4'],rate=0.7)
	p1000.dispense(900.00,reservoir['A9'],rate=0.7)
	p300.drop_tip()
	p1000.drop_tip()
	#Vol_NH4Cl
	p300.pick_up_tip()
	p1000.pick_up_tip()
	p300.aspirate(271.0,big1['A4'],rate=0.7)
	p300.dispense(271.0,reservoir['A10'],rate=0.7)
	p1000.aspirate(664.75,big1['A4'],rate=0.7)
	p1000.dispense(664.75,reservoir['A11'],rate=0.7)
	p1000.aspirate(664.75,big1['A4'],rate=0.7)
	p1000.dispense(664.75,reservoir['A11'],rate=0.7)
	p1000.aspirate(681.3,big1['A4'],rate=0.7)
	p1000.dispense(681.3,reservoir['A12'],rate=0.7)
	p1000.aspirate(873.80,big1['A4'],rate=0.7)
	p1000.dispense(873.80,reservoir['B1'],rate=0.7)
	p1000.aspirate(873.80,big1['A4'],rate=0.7)
	p1000.dispense(873.80,reservoir['B1'],rate=0.7)
	p1000.aspirate(858.3,big1['A4'],rate=0.7)
	p1000.dispense(858.3,reservoir['B2'],rate=0.7)
	p1000.aspirate(896.00,big1['A4'],rate=0.7)
	p1000.dispense(896.00,reservoir['B3'],rate=0.7)
	p1000.aspirate(896.00,big1['A4'],rate=0.7)
	p1000.dispense(896.00,reservoir['B3'],rate=0.7)
	p300.aspirate(189.5,big1['A4'],rate=0.7)
	p300.dispense(189.5,reservoir['B4'],rate=0.7)
	p300.aspirate(155.8,big1['A4'],rate=0.7)
	p300.dispense(155.8,reservoir['B5'],rate=0.7)
	p300.aspirate(155.8,big1['A4'],rate=0.7)
	p300.dispense(155.8,reservoir['B6'],rate=0.7)
	p300.drop_tip()
	p1000.drop_tip()
	#Water_NH4Cl
	p300.pick_up_tip()
	p1000.pick_up_tip()
	p1000.aspirate(864.50,big2['B4'],rate=0.7)
	p1000.dispense(864.50,reservoir['A10'],rate=0.7)
	p1000.aspirate(864.50,big2['B4'],rate=0.7)
	p1000.dispense(864.50,reservoir['A10'],rate=0.7)
	p1000.aspirate(670.5,big2['B4'],rate=0.7)
	p1000.dispense(670.5,reservoir['A11'],rate=0.7)
	p1000.aspirate(659.35,big2['B4'],rate=0.7)
	p1000.dispense(659.35,reservoir['A12'],rate=0.7)
	p1000.aspirate(659.35,big2['B4'],rate=0.7)
	p1000.dispense(659.35,reservoir['A12'],rate=0.7)
	p300.aspirate(252.4,big2['B4'],rate=0.7)
	p300.dispense(252.4,reservoir['B1'],rate=0.7)
	p1000.aspirate(570.85,big2['B4'],rate=0.7)
	p1000.dispense(570.85,reservoir['B2'],rate=0.7)
	p1000.aspirate(570.85,big2['B4'],rate=0.7)
	p1000.dispense(570.85,reservoir['B2'],rate=0.7)
	p300.aspirate(208.0,big2['B4'],rate=0.7)
	p300.dispense(208.0,reservoir['B3'],rate=0.7)
	p1000.aspirate(905.25,big2['B4'],rate=0.7)
	p1000.dispense(905.25,reservoir['B4'],rate=0.7)
	p1000.aspirate(905.25,big2['B4'],rate=0.7)
	p1000.dispense(905.25,reservoir['B4'],rate=0.7)
	p1000.aspirate(922.10,big2['B4'],rate=0.7)
	p1000.dispense(922.10,reservoir['B5'],rate=0.7)
	p1000.aspirate(922.10,big2['B4'],rate=0.7)
	p1000.dispense(922.10,reservoir['B5'],rate=0.7)
	p1000.aspirate(922.10,big2['B4'],rate=0.7)
	p1000.dispense(922.10,reservoir['B6'],rate=0.7)
	p1000.aspirate(922.10,big2['B4'],rate=0.7)
	p1000.dispense(922.10,reservoir['B6'],rate=0.7)
	p300.drop_tip()
	p1000.drop_tip()
	#Vol_MgSO4
	p300.pick_up_tip()
	p1000.pick_up_tip()
	p300.aspirate(282.9,big1['B3'],rate=0.7)
	p300.dispense(282.9,reservoir['B7'],rate=0.7)
	p1000.aspirate(929.95,big1['B3'],rate=0.7)
	p1000.dispense(929.95,reservoir['B8'],rate=0.7)
	p1000.aspirate(929.95,big1['B3'],rate=0.7)
	p1000.dispense(929.95,reservoir['B8'],rate=0.7)
	p1000.aspirate(596.1,big1['B3'],rate=0.7)
	p1000.dispense(596.1,reservoir['B9'],rate=0.7)
	p1000.aspirate(525.05,big1['B3'],rate=0.7)
	p1000.dispense(525.05,reservoir['B10'],rate=0.7)
	p1000.aspirate(525.05,big1['B3'],rate=0.7)
	p1000.dispense(525.05,reservoir['B10'],rate=0.7)
	p1000.aspirate(762.65,big1['B3'],rate=0.7)
	p1000.dispense(762.65,reservoir['B11'],rate=0.7)
	p1000.aspirate(762.65,big1['B3'],rate=0.7)
	p1000.dispense(762.65,reservoir['B11'],rate=0.7)
	p300.aspirate(71.2,big1['B3'],rate=0.7)
	p300.dispense(71.2,reservoir['B12'],rate=0.7)
	p1000.aspirate(669.05,big1['B3'],rate=0.7)
	p1000.dispense(669.05,reservoir['C1'],rate=0.7)
	p1000.aspirate(669.05,big1['B3'],rate=0.7)
	p1000.dispense(669.05,reservoir['C1'],rate=0.7)
	p1000.aspirate(1000.00,big1['B3'],rate=0.7)
	p1000.dispense(1000.00,reservoir['C2'],rate=0.7)
	p1000.aspirate(1000.00,big1['B3'],rate=0.7)
	p1000.dispense(1000.00,reservoir['C2'],rate=0.7)
	p1000.aspirate(1000.00,big1['B3'],rate=0.7)
	p1000.dispense(1000.00,reservoir['C3'],rate=0.7)
	p1000.aspirate(1000.00,big1['B3'],rate=0.7)
	p1000.dispense(1000.00,reservoir['C3'],rate=0.7)
	p300.drop_tip()
	p1000.drop_tip()
	#Water_MgSO4
	p300.pick_up_tip()
	p1000.pick_up_tip()
	p1000.aspirate(858.55,big2['B4'],rate=0.7)
	p1000.dispense(858.55,reservoir['B7'],rate=0.7)
	p1000.aspirate(858.55,big2['B4'],rate=0.7)
	p1000.dispense(858.55,reservoir['B7'],rate=0.7)
	p300.aspirate(140.1,big2['B4'],rate=0.7)
	p300.dispense(140.1,reservoir['B8'],rate=0.7)
	p1000.aspirate(701.95,big2['B4'],rate=0.7)
	p1000.dispense(701.95,reservoir['B9'],rate=0.7)
	p1000.aspirate(701.95,big2['B4'],rate=0.7)
	p1000.dispense(701.95,reservoir['B9'],rate=0.7)
	p1000.aspirate(949.9,big2['B4'],rate=0.7)
	p1000.dispense(949.9,reservoir['B10'],rate=0.7)
	p1000.aspirate(474.7,big2['B4'],rate=0.7)
	p1000.dispense(474.7,reservoir['B11'],rate=0.7)
	p1000.aspirate(964.40,big2['B4'],rate=0.7)
	p1000.dispense(964.40,reservoir['B12'],rate=0.7)
	p1000.aspirate(964.40,big2['B4'],rate=0.7)
	p1000.dispense(964.40,reservoir['B12'],rate=0.7)
	p1000.aspirate(661.9,big2['B4'],rate=0.7)
	p1000.dispense(661.9,reservoir['C1'],rate=0.7)
	p300.drop_tip()
	p1000.drop_tip()
	#Vol_KH2PO4
	p1000.pick_up_tip()
	p1000.aspirate(320.9,big1['B4'],rate=0.7)
	p1000.dispense(320.9,reservoir['C4'],rate=0.7)
	p1000.aspirate(587.70,big1['B4'],rate=0.7)
	p1000.dispense(587.70,reservoir['C5'],rate=0.7)
	p1000.aspirate(587.70,big1['B4'],rate=0.7)
	p1000.dispense(587.70,reservoir['C5'],rate=0.7)
	p1000.aspirate(929.8,big1['B4'],rate=0.7)
	p1000.dispense(929.8,reservoir['C6'],rate=0.7)
	p1000.aspirate(782.80,big1['B4'],rate=0.7)
	p1000.dispense(782.80,reservoir['C7'],rate=0.7)
	p1000.aspirate(782.80,big1['B4'],rate=0.7)
	p1000.dispense(782.80,reservoir['C7'],rate=0.7)
	p1000.aspirate(928.50,big1['B4'],rate=0.7)
	p1000.dispense(928.50,reservoir['C8'],rate=0.7)
	p1000.aspirate(928.50,big1['B4'],rate=0.7)
	p1000.dispense(928.50,reservoir['C8'],rate=0.7)
	p1000.aspirate(647.2,big1['B4'],rate=0.7)
	p1000.dispense(647.2,reservoir['C9'],rate=0.7)
	p1000.aspirate(701.70,big1['B4'],rate=0.7)
	p1000.dispense(701.70,reservoir['C10'],rate=0.7)
	p1000.aspirate(701.70,big1['B4'],rate=0.7)
	p1000.dispense(701.70,reservoir['C10'],rate=0.7)
	p1000.aspirate(881.6,big1['B4'],rate=0.7)
	p1000.dispense(881.6,reservoir['C11'],rate=0.7)
	p1000.aspirate(881.6,big1['B4'],rate=0.7)
	p1000.dispense(881.6,reservoir['C12'],rate=0.7)
	p1000.drop_tip()
	#Water_KH2PO4
	p300.pick_up_tip()
	p1000.pick_up_tip()
	p1000.aspirate(839.55,big2['B4'],rate=0.7)
	p1000.dispense(839.55,reservoir['C4'],rate=0.7)
	p1000.aspirate(839.55,big2['B4'],rate=0.7)
	p1000.dispense(839.55,reservoir['C4'],rate=0.7)
	p1000.aspirate(824.6,big2['B4'],rate=0.7)
	p1000.dispense(824.6,reservoir['C5'],rate=0.7)
	p1000.aspirate(535.10,big2['B4'],rate=0.7)
	p1000.dispense(535.10,reservoir['C6'],rate=0.7)
	p1000.aspirate(535.10,big2['B4'],rate=0.7)
	p1000.dispense(535.10,reservoir['C6'],rate=0.7)
	p1000.aspirate(434.4,big2['B4'],rate=0.7)
	p1000.dispense(434.4,reservoir['C7'],rate=0.7)
	p300.aspirate(143.0,big2['B4'],rate=0.7)
	p300.dispense(143.0,reservoir['C8'],rate=0.7)
	p1000.aspirate(676.40,big2['B4'],rate=0.7)
	p1000.dispense(676.40,reservoir['C9'],rate=0.7)
	p1000.aspirate(676.40,big2['B4'],rate=0.7)
	p1000.dispense(676.40,reservoir['C9'],rate=0.7)
	p1000.aspirate(596.6,big2['B4'],rate=0.7)
	p1000.dispense(596.6,reservoir['C10'],rate=0.7)
	p1000.aspirate(559.20,big2['B4'],rate=0.7)
	p1000.dispense(559.20,reservoir['C11'],rate=0.7)
	p1000.aspirate(559.20,big2['B4'],rate=0.7)
	p1000.dispense(559.20,reservoir['C11'],rate=0.7)
	p1000.aspirate(559.20,big2['B4'],rate=0.7)
	p1000.dispense(559.20,reservoir['C12'],rate=0.7)
	p1000.aspirate(559.20,big2['B4'],rate=0.7)
	p1000.dispense(559.20,reservoir['C12'],rate=0.7)
	p300.drop_tip()
	p1000.drop_tip()
	#Vol_Na2HPO4
	p300.pick_up_tip()
	p1000.pick_up_tip()
	p1000.aspirate(965.75,big2['A3'],rate=0.7)
	p1000.dispense(965.75,reservoir['D1'],rate=0.7)
	p1000.aspirate(965.75,big2['A3'],rate=0.7)
	p1000.dispense(965.75,reservoir['D1'],rate=0.7)
	p1000.aspirate(438.4,big2['A3'],rate=0.7)
	p1000.dispense(438.4,reservoir['D2'],rate=0.7)
	p1000.aspirate(649.8,big2['A3'],rate=0.7)
	p1000.dispense(649.8,reservoir['D3'],rate=0.7)
	p1000.aspirate(609.55,big2['A3'],rate=0.7)
	p1000.dispense(609.55,reservoir['D4'],rate=0.7)
	p1000.aspirate(609.55,big2['A3'],rate=0.7)
	p1000.dispense(609.55,reservoir['D4'],rate=0.7)
	p1000.aspirate(679.75,big2['A3'],rate=0.7)
	p1000.dispense(679.75,reservoir['D5'],rate=0.7)
	p1000.aspirate(679.75,big2['A3'],rate=0.7)
	p1000.dispense(679.75,reservoir['D5'],rate=0.7)
	p1000.aspirate(759.0,big2['A3'],rate=0.7)
	p1000.dispense(759.0,reservoir['D6'],rate=0.7)
	p300.aspirate(78.8,big2['A3'],rate=0.7)
	p300.dispense(78.8,reservoir['D7'],rate=0.7)
	p1000.aspirate(845.20,big2['A3'],rate=0.7)
	p1000.dispense(845.20,reservoir['D8'],rate=0.7)
	p1000.aspirate(845.20,big2['A3'],rate=0.7)
	p1000.dispense(845.20,reservoir['D8'],rate=0.7)
	p1000.aspirate(845.20,big2['A3'],rate=0.7)
	p1000.dispense(845.20,reservoir['D9'],rate=0.7)
	p1000.aspirate(845.20,big2['A3'],rate=0.7)
	p1000.dispense(845.20,reservoir['D9'],rate=0.7)
	p300.drop_tip()
	p1000.drop_tip()
	#Water_Na2HPO4
	p300.pick_up_tip()
	p1000.pick_up_tip()
	p300.aspirate(68.5,big2['B4'],rate=0.7)
	p300.dispense(68.5,reservoir['D1'],rate=0.7)
	p1000.aspirate(780.80,big2['B4'],rate=0.7)
	p1000.dispense(780.80,reservoir['D2'],rate=0.7)
	p1000.aspirate(780.80,big2['B4'],rate=0.7)
	p1000.dispense(780.80,reservoir['D2'],rate=0.7)
	p1000.aspirate(675.10,big2['B4'],rate=0.7)
	p1000.dispense(675.10,reservoir['D3'],rate=0.7)
	p1000.aspirate(675.10,big2['B4'],rate=0.7)
	p1000.dispense(675.10,reservoir['D3'],rate=0.7)
	p1000.aspirate(780.9,big2['B4'],rate=0.7)
	p1000.dispense(780.9,reservoir['D4'],rate=0.7)
	p1000.aspirate(640.5,big2['B4'],rate=0.7)
	p1000.dispense(640.5,reservoir['D5'],rate=0.7)
	p1000.aspirate(620.50,big2['B4'],rate=0.7)
	p1000.dispense(620.50,reservoir['D6'],rate=0.7)
	p1000.aspirate(620.50,big2['B4'],rate=0.7)
	p1000.dispense(620.50,reservoir['D6'],rate=0.7)
	p1000.aspirate(960.60,big2['B4'],rate=0.7)
	p1000.dispense(960.60,reservoir['D7'],rate=0.7)
	p1000.aspirate(960.60,big2['B4'],rate=0.7)
	p1000.dispense(960.60,reservoir['D7'],rate=0.7)
	p1000.aspirate(309.6,big2['B4'],rate=0.7)
	p1000.dispense(309.6,reservoir['D8'],rate=0.7)
	p1000.aspirate(309.6,big2['B4'],rate=0.7)
	p1000.dispense(309.6,reservoir['D9'],rate=0.7)
	p300.drop_tip()
	p1000.drop_tip()
	#Vol_CaCl2
	p300.pick_up_tip()
	p1000.pick_up_tip()
	p1000.aspirate(859.40,big2['A4'],rate=0.7)
	p1000.dispense(859.40,reservoir['D10'],rate=0.7)
	p1000.aspirate(859.40,big2['A4'],rate=0.7)
	p1000.dispense(859.40,reservoir['D10'],rate=0.7)
	p300.aspirate(285.7,big2['A4'],rate=0.7)
	p300.dispense(285.7,reservoir['D11'],rate=0.7)
	p1000.aspirate(527.9,big2['A4'],rate=0.7)
	p1000.dispense(527.9,reservoir['D12'],rate=0.7)
	p1000.aspirate(730.50,big2['A4'],rate=0.7)
	p1000.dispense(730.50,reservoir['E1'],rate=0.7)
	p1000.aspirate(730.50,big2['A4'],rate=0.7)
	p1000.dispense(730.50,reservoir['E1'],rate=0.7)
	p1000.aspirate(937.35,big2['A4'],rate=0.7)
	p1000.dispense(937.35,reservoir['E2'],rate=0.7)
	p1000.aspirate(937.35,big2['A4'],rate=0.7)
	p1000.dispense(937.35,reservoir['E2'],rate=0.7)
	p300.aspirate(182.8,big2['A4'],rate=0.7)
	p300.dispense(182.8,reservoir['E3'],rate=0.7)
	p1000.aspirate(878.1,big2['A4'],rate=0.7)
	p1000.dispense(878.1,reservoir['E4'],rate=0.7)
	p1000.aspirate(1000.0,big2['A4'],rate=0.7)
	p1000.dispense(1000.0,reservoir['E5'],rate=0.7)
	p1000.aspirate(1000.0,big2['A4'],rate=0.7)
	p1000.dispense(1000.0,reservoir['E6'],rate=0.7)
	p300.drop_tip()
	p1000.drop_tip()
	#Water_CaCl2
	p300.pick_up_tip()
	p1000.pick_up_tip()
	p300.aspirate(281.2,big2['B4'],rate=0.7)
	p300.dispense(281.2,reservoir['D10'],rate=0.7)
	p1000.aspirate(857.15,big2['B4'],rate=0.7)
	p1000.dispense(857.15,reservoir['D11'],rate=0.7)
	p1000.aspirate(857.15,big2['B4'],rate=0.7)
	p1000.dispense(857.15,reservoir['D11'],rate=0.7)
	p1000.aspirate(736.05,big2['B4'],rate=0.7)
	p1000.dispense(736.05,reservoir['D12'],rate=0.7)
	p1000.aspirate(736.05,big2['B4'],rate=0.7)
	p1000.dispense(736.05,reservoir['D12'],rate=0.7)
	p1000.aspirate(539.0,big2['B4'],rate=0.7)
	p1000.dispense(539.0,reservoir['E1'],rate=0.7)
	p300.aspirate(125.3,big2['B4'],rate=0.7)
	p300.dispense(125.3,reservoir['E2'],rate=0.7)
	p1000.aspirate(908.60,big2['B4'],rate=0.7)
	p1000.dispense(908.60,reservoir['E3'],rate=0.7)
	p1000.aspirate(908.60,big2['B4'],rate=0.7)
	p1000.dispense(908.60,reservoir['E3'],rate=0.7)
	p1000.aspirate(560.95,big2['B4'],rate=0.7)
	p1000.dispense(560.95,reservoir['E4'],rate=0.7)
	p1000.aspirate(560.95,big2['B4'],rate=0.7)
	p1000.dispense(560.95,reservoir['E4'],rate=0.7)
	p1000.aspirate(1000.0,big2['B4'],rate=0.7)
	p1000.dispense(1000.0,reservoir['E5'],rate=0.7)
	p1000.aspirate(1000.0,big2['B4'],rate=0.7)
	p1000.dispense(1000.0,reservoir['E6'],rate=0.7)
	p300.drop_tip()
	p1000.drop_tip()
	#Vol_NaCl
	p1000.pick_up_tip()
	p1000.aspirate(570.00,big2['B3'],rate=0.7)
	p1000.dispense(570.00,reservoir['E7'],rate=0.7)
	p1000.aspirate(570.00,big2['B3'],rate=0.7)
	p1000.dispense(570.00,reservoir['E7'],rate=0.7)
	p1000.aspirate(479.3,big2['B3'],rate=0.7)
	p1000.dispense(479.3,reservoir['E8'],rate=0.7)
	p1000.aspirate(801.70,big2['B3'],rate=0.7)
	p1000.dispense(801.70,reservoir['E9'],rate=0.7)
	p1000.aspirate(801.70,big2['B3'],rate=0.7)
	p1000.dispense(801.70,reservoir['E9'],rate=0.7)
	p1000.aspirate(762.1,big2['B3'],rate=0.7)
	p1000.dispense(762.1,reservoir['E10'],rate=0.7)
	p1000.aspirate(931.50,big2['B3'],rate=0.7)
	p1000.dispense(931.50,reservoir['E11'],rate=0.7)
	p1000.aspirate(931.50,big2['B3'],rate=0.7)
	p1000.dispense(931.50,reservoir['E11'],rate=0.7)
	p1000.aspirate(521.6,big2['B3'],rate=0.7)
	p1000.dispense(521.6,reservoir['E12'],rate=0.7)
	p1000.aspirate(697.80,big2['B3'],rate=0.7)
	p1000.dispense(697.80,reservoir['F1'],rate=0.7)
	p1000.aspirate(697.80,big2['B3'],rate=0.7)
	p1000.dispense(697.80,reservoir['F1'],rate=0.7)
	p1000.aspirate(342.0,big2['B3'],rate=0.7)
	p1000.dispense(342.0,reservoir['F2'],rate=0.7)
	p1000.aspirate(342.0,big2['B3'],rate=0.7)
	p1000.dispense(342.0,reservoir['F3'],rate=0.7)
	p1000.drop_tip()
	#Water_NaCl
	p300.pick_up_tip()
	p1000.pick_up_tip()
	p1000.aspirate(860.0,big2['B4'],rate=0.7)
	p1000.dispense(860.0,reservoir['E7'],rate=0.7)
	p1000.aspirate(760.35,big2['B4'],rate=0.7)
	p1000.dispense(760.35,reservoir['E8'],rate=0.7)
	p1000.aspirate(760.35,big2['B4'],rate=0.7)
	p1000.dispense(760.35,reservoir['E8'],rate=0.7)
	p1000.aspirate(396.6,big2['B4'],rate=0.7)
	p1000.dispense(396.6,reservoir['E9'],rate=0.7)
	p1000.aspirate(618.95,big2['B4'],rate=0.7)
	p1000.dispense(618.95,reservoir['E10'],rate=0.7)
	p1000.aspirate(618.95,big2['B4'],rate=0.7)
	p1000.dispense(618.95,reservoir['E10'],rate=0.7)
	p300.aspirate(137.0,big2['B4'],rate=0.7)
	p300.dispense(137.0,reservoir['E11'],rate=0.7)
	p1000.aspirate(739.20,big2['B4'],rate=0.7)
	p1000.dispense(739.20,reservoir['E12'],rate=0.7)
	p1000.aspirate(739.20,big2['B4'],rate=0.7)
	p1000.dispense(739.20,reservoir['E12'],rate=0.7)
	p1000.aspirate(604.4,big2['B4'],rate=0.7)
	p1000.dispense(604.4,reservoir['F1'],rate=0.7)
	p1000.aspirate(829.00,big2['B4'],rate=0.7)
	p1000.dispense(829.00,reservoir['F2'],rate=0.7)
	p1000.aspirate(829.00,big2['B4'],rate=0.7)
	p1000.dispense(829.00,reservoir['F2'],rate=0.7)
	p1000.aspirate(829.00,big2['B4'],rate=0.7)
	p1000.dispense(829.00,reservoir['F3'],rate=0.7)
	p1000.aspirate(829.00,big2['B4'],rate=0.7)
	p1000.dispense(829.00,reservoir['F3'],rate=0.7)
	p300.drop_tip()
	p1000.drop_tip()
