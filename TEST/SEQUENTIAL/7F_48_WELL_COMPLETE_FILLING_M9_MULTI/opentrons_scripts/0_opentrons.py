from opentrons import protocol_api
metadata = {'apiLevel': '2.13'}
def run(protocol: protocol_api.ProtocolContext):
	plate = protocol.load_labware('corning_48_wellplate_1.6ml_flat', 8)
	tiprack_2 = protocol.load_labware('opentrons_96_tiprack_300ul', 11)
	reservoir = protocol.load_labware('nest_96_wellplate_2ml_deep',5)
	big= protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical',6)
	p300 = protocol.load_instrument('p300_single', 'left', tip_racks=[tiprack_2])
	#Glucose_0_1
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['A1'],rate=0.7)
	p300.dispense(80, plate['B4'],rate=0.7)
	p300.aspirate(80, reservoir['A1'],rate=0.7)
	p300.dispense(80, plate['A7'],rate=0.7)
	p300.aspirate(80, reservoir['A1'],rate=0.7)
	p300.dispense(80, plate['F4'],rate=0.7)
	p300.aspirate(80, reservoir['A1'],rate=0.7)
	p300.dispense(80, plate['D5'],rate=0.7)
	p300.drop_tip()
	#NH4Cl_0_1
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['A10'],rate=0.7)
	p300.dispense(80, plate['B4'],rate=0.7)
	p300.aspirate(80, reservoir['A10'],rate=0.7)
	p300.dispense(80, plate['A7'],rate=0.7)
	p300.aspirate(80, reservoir['A10'],rate=0.7)
	p300.dispense(80, plate['F4'],rate=0.7)
	p300.aspirate(80, reservoir['A10'],rate=0.7)
	p300.dispense(80, plate['D5'],rate=0.7)
	p300.drop_tip()
	#MgSO4_0_1
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['B7'],rate=0.7)
	p300.dispense(80, plate['B4'],rate=0.7)
	p300.aspirate(80, reservoir['B7'],rate=0.7)
	p300.dispense(80, plate['A7'],rate=0.7)
	p300.aspirate(80, reservoir['B7'],rate=0.7)
	p300.dispense(80, plate['F4'],rate=0.7)
	p300.aspirate(80, reservoir['B7'],rate=0.7)
	p300.dispense(80, plate['D5'],rate=0.7)
	p300.drop_tip()
	#KH2PO4_0_1
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['C4'],rate=0.7)
	p300.dispense(80, plate['B4'],rate=0.7)
	p300.aspirate(80, reservoir['C4'],rate=0.7)
	p300.dispense(80, plate['A7'],rate=0.7)
	p300.aspirate(80, reservoir['C4'],rate=0.7)
	p300.dispense(80, plate['F4'],rate=0.7)
	p300.aspirate(80, reservoir['C4'],rate=0.7)
	p300.dispense(80, plate['D5'],rate=0.7)
	p300.drop_tip()
	#Na2HPO4_0_1
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['D1'],rate=0.7)
	p300.dispense(80, plate['B4'],rate=0.7)
	p300.aspirate(80, reservoir['D1'],rate=0.7)
	p300.dispense(80, plate['A7'],rate=0.7)
	p300.aspirate(80, reservoir['D1'],rate=0.7)
	p300.dispense(80, plate['F4'],rate=0.7)
	p300.aspirate(80, reservoir['D1'],rate=0.7)
	p300.dispense(80, plate['D5'],rate=0.7)
	p300.drop_tip()
	#CaCl2_0_1
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['D10'],rate=0.7)
	p300.dispense(80, plate['B4'],rate=0.7)
	p300.aspirate(80, reservoir['D10'],rate=0.7)
	p300.dispense(80, plate['A7'],rate=0.7)
	p300.aspirate(80, reservoir['D10'],rate=0.7)
	p300.dispense(80, plate['F4'],rate=0.7)
	p300.aspirate(80, reservoir['D10'],rate=0.7)
	p300.dispense(80, plate['D5'],rate=0.7)
	p300.drop_tip()
	#NaCl_0_1
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['E7'],rate=0.7)
	p300.dispense(80, plate['B4'],rate=0.7)
	p300.aspirate(80, reservoir['E7'],rate=0.7)
	p300.dispense(80, plate['A7'],rate=0.7)
	p300.aspirate(80, reservoir['E7'],rate=0.7)
	p300.dispense(80, plate['F4'],rate=0.7)
	p300.aspirate(80, reservoir['E7'],rate=0.7)
	p300.dispense(80, plate['D5'],rate=0.7)
	p300.drop_tip()
	#Glucose_0_2
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['A2'],rate=0.7)
	p300.dispense(80, plate['B2'],rate=0.7)
	p300.aspirate(80, reservoir['A2'],rate=0.7)
	p300.dispense(80, plate['F6'],rate=0.7)
	p300.aspirate(80, reservoir['A2'],rate=0.7)
	p300.dispense(80, plate['A6'],rate=0.7)
	p300.aspirate(80, reservoir['A2'],rate=0.7)
	p300.dispense(80, plate['D3'],rate=0.7)
	p300.drop_tip()
	#NH4Cl_0_2
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['A11'],rate=0.7)
	p300.dispense(80, plate['B2'],rate=0.7)
	p300.aspirate(80, reservoir['A11'],rate=0.7)
	p300.dispense(80, plate['F6'],rate=0.7)
	p300.aspirate(80, reservoir['A11'],rate=0.7)
	p300.dispense(80, plate['A6'],rate=0.7)
	p300.aspirate(80, reservoir['A11'],rate=0.7)
	p300.dispense(80, plate['D3'],rate=0.7)
	p300.drop_tip()
	#MgSO4_0_2
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['B8'],rate=0.7)
	p300.dispense(80, plate['B2'],rate=0.7)
	p300.aspirate(80, reservoir['B8'],rate=0.7)
	p300.dispense(80, plate['F6'],rate=0.7)
	p300.aspirate(80, reservoir['B8'],rate=0.7)
	p300.dispense(80, plate['A6'],rate=0.7)
	p300.aspirate(80, reservoir['B8'],rate=0.7)
	p300.dispense(80, plate['D3'],rate=0.7)
	p300.drop_tip()
	#KH2PO4_0_2
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['C5'],rate=0.7)
	p300.dispense(80, plate['B2'],rate=0.7)
	p300.aspirate(80, reservoir['C5'],rate=0.7)
	p300.dispense(80, plate['F6'],rate=0.7)
	p300.aspirate(80, reservoir['C5'],rate=0.7)
	p300.dispense(80, plate['A6'],rate=0.7)
	p300.aspirate(80, reservoir['C5'],rate=0.7)
	p300.dispense(80, plate['D3'],rate=0.7)
	p300.drop_tip()
	#Na2HPO4_0_2
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['D2'],rate=0.7)
	p300.dispense(80, plate['B2'],rate=0.7)
	p300.aspirate(80, reservoir['D2'],rate=0.7)
	p300.dispense(80, plate['F6'],rate=0.7)
	p300.aspirate(80, reservoir['D2'],rate=0.7)
	p300.dispense(80, plate['A6'],rate=0.7)
	p300.aspirate(80, reservoir['D2'],rate=0.7)
	p300.dispense(80, plate['D3'],rate=0.7)
	p300.drop_tip()
	#CaCl2_0_2
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['D11'],rate=0.7)
	p300.dispense(80, plate['B2'],rate=0.7)
	p300.aspirate(80, reservoir['D11'],rate=0.7)
	p300.dispense(80, plate['F6'],rate=0.7)
	p300.aspirate(80, reservoir['D11'],rate=0.7)
	p300.dispense(80, plate['A6'],rate=0.7)
	p300.aspirate(80, reservoir['D11'],rate=0.7)
	p300.dispense(80, plate['D3'],rate=0.7)
	p300.drop_tip()
	#NaCl_0_2
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['E8'],rate=0.7)
	p300.dispense(80, plate['B2'],rate=0.7)
	p300.aspirate(80, reservoir['E8'],rate=0.7)
	p300.dispense(80, plate['F6'],rate=0.7)
	p300.aspirate(80, reservoir['E8'],rate=0.7)
	p300.dispense(80, plate['A6'],rate=0.7)
	p300.aspirate(80, reservoir['E8'],rate=0.7)
	p300.dispense(80, plate['D3'],rate=0.7)
	p300.drop_tip()
	#Glucose_0_3
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['A3'],rate=0.7)
	p300.dispense(80, plate['E4'],rate=0.7)
	p300.aspirate(80, reservoir['A3'],rate=0.7)
	p300.dispense(80, plate['C2'],rate=0.7)
	p300.aspirate(80, reservoir['A3'],rate=0.7)
	p300.dispense(80, plate['B5'],rate=0.7)
	p300.aspirate(80, reservoir['A3'],rate=0.7)
	p300.dispense(80, plate['D6'],rate=0.7)
	p300.drop_tip()
	#NH4Cl_0_3
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['A12'],rate=0.7)
	p300.dispense(80, plate['E4'],rate=0.7)
	p300.aspirate(80, reservoir['A12'],rate=0.7)
	p300.dispense(80, plate['C2'],rate=0.7)
	p300.aspirate(80, reservoir['A12'],rate=0.7)
	p300.dispense(80, plate['B5'],rate=0.7)
	p300.aspirate(80, reservoir['A12'],rate=0.7)
	p300.dispense(80, plate['D6'],rate=0.7)
	p300.drop_tip()
	#MgSO4_0_3
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['B9'],rate=0.7)
	p300.dispense(80, plate['E4'],rate=0.7)
	p300.aspirate(80, reservoir['B9'],rate=0.7)
	p300.dispense(80, plate['C2'],rate=0.7)
	p300.aspirate(80, reservoir['B9'],rate=0.7)
	p300.dispense(80, plate['B5'],rate=0.7)
	p300.aspirate(80, reservoir['B9'],rate=0.7)
	p300.dispense(80, plate['D6'],rate=0.7)
	p300.drop_tip()
	#KH2PO4_0_3
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['C6'],rate=0.7)
	p300.dispense(80, plate['E4'],rate=0.7)
	p300.aspirate(80, reservoir['C6'],rate=0.7)
	p300.dispense(80, plate['C2'],rate=0.7)
	p300.aspirate(80, reservoir['C6'],rate=0.7)
	p300.dispense(80, plate['B5'],rate=0.7)
	p300.aspirate(80, reservoir['C6'],rate=0.7)
	p300.dispense(80, plate['D6'],rate=0.7)
	p300.drop_tip()
	#Na2HPO4_0_3
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['D3'],rate=0.7)
	p300.dispense(80, plate['E4'],rate=0.7)
	p300.aspirate(80, reservoir['D3'],rate=0.7)
	p300.dispense(80, plate['C2'],rate=0.7)
	p300.aspirate(80, reservoir['D3'],rate=0.7)
	p300.dispense(80, plate['B5'],rate=0.7)
	p300.aspirate(80, reservoir['D3'],rate=0.7)
	p300.dispense(80, plate['D6'],rate=0.7)
	p300.drop_tip()
	#CaCl2_0_3
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['D12'],rate=0.7)
	p300.dispense(80, plate['E4'],rate=0.7)
	p300.aspirate(80, reservoir['D12'],rate=0.7)
	p300.dispense(80, plate['C2'],rate=0.7)
	p300.aspirate(80, reservoir['D12'],rate=0.7)
	p300.dispense(80, plate['B5'],rate=0.7)
	p300.aspirate(80, reservoir['D12'],rate=0.7)
	p300.dispense(80, plate['D6'],rate=0.7)
	p300.drop_tip()
	#NaCl_0_3
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['E9'],rate=0.7)
	p300.dispense(80, plate['E4'],rate=0.7)
	p300.aspirate(80, reservoir['E9'],rate=0.7)
	p300.dispense(80, plate['C2'],rate=0.7)
	p300.aspirate(80, reservoir['E9'],rate=0.7)
	p300.dispense(80, plate['B5'],rate=0.7)
	p300.aspirate(80, reservoir['E9'],rate=0.7)
	p300.dispense(80, plate['D6'],rate=0.7)
	p300.drop_tip()
	#Glucose_0_4
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['A4'],rate=0.7)
	p300.dispense(80, plate['C5'],rate=0.7)
	p300.aspirate(80, reservoir['A4'],rate=0.7)
	p300.dispense(80, plate['F3'],rate=0.7)
	p300.aspirate(80, reservoir['A4'],rate=0.7)
	p300.dispense(80, plate['E7'],rate=0.7)
	p300.aspirate(80, reservoir['A4'],rate=0.7)
	p300.dispense(80, plate['A2'],rate=0.7)
	p300.drop_tip()
	#NH4Cl_0_4
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['B1'],rate=0.7)
	p300.dispense(80, plate['C5'],rate=0.7)
	p300.aspirate(80, reservoir['B1'],rate=0.7)
	p300.dispense(80, plate['F3'],rate=0.7)
	p300.aspirate(80, reservoir['B1'],rate=0.7)
	p300.dispense(80, plate['E7'],rate=0.7)
	p300.aspirate(80, reservoir['B1'],rate=0.7)
	p300.dispense(80, plate['A2'],rate=0.7)
	p300.drop_tip()
	#MgSO4_0_4
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['B10'],rate=0.7)
	p300.dispense(80, plate['C5'],rate=0.7)
	p300.aspirate(80, reservoir['B10'],rate=0.7)
	p300.dispense(80, plate['F3'],rate=0.7)
	p300.aspirate(80, reservoir['B10'],rate=0.7)
	p300.dispense(80, plate['E7'],rate=0.7)
	p300.aspirate(80, reservoir['B10'],rate=0.7)
	p300.dispense(80, plate['A2'],rate=0.7)
	p300.drop_tip()
	#KH2PO4_0_4
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['C7'],rate=0.7)
	p300.dispense(80, plate['C5'],rate=0.7)
	p300.aspirate(80, reservoir['C7'],rate=0.7)
	p300.dispense(80, plate['F3'],rate=0.7)
	p300.aspirate(80, reservoir['C7'],rate=0.7)
	p300.dispense(80, plate['E7'],rate=0.7)
	p300.aspirate(80, reservoir['C7'],rate=0.7)
	p300.dispense(80, plate['A2'],rate=0.7)
	p300.drop_tip()
	#Na2HPO4_0_4
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['D4'],rate=0.7)
	p300.dispense(80, plate['C5'],rate=0.7)
	p300.aspirate(80, reservoir['D4'],rate=0.7)
	p300.dispense(80, plate['F3'],rate=0.7)
	p300.aspirate(80, reservoir['D4'],rate=0.7)
	p300.dispense(80, plate['E7'],rate=0.7)
	p300.aspirate(80, reservoir['D4'],rate=0.7)
	p300.dispense(80, plate['A2'],rate=0.7)
	p300.drop_tip()
	#CaCl2_0_4
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['E1'],rate=0.7)
	p300.dispense(80, plate['C5'],rate=0.7)
	p300.aspirate(80, reservoir['E1'],rate=0.7)
	p300.dispense(80, plate['F3'],rate=0.7)
	p300.aspirate(80, reservoir['E1'],rate=0.7)
	p300.dispense(80, plate['E7'],rate=0.7)
	p300.aspirate(80, reservoir['E1'],rate=0.7)
	p300.dispense(80, plate['A2'],rate=0.7)
	p300.drop_tip()
	#NaCl_0_4
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['E10'],rate=0.7)
	p300.dispense(80, plate['C5'],rate=0.7)
	p300.aspirate(80, reservoir['E10'],rate=0.7)
	p300.dispense(80, plate['F3'],rate=0.7)
	p300.aspirate(80, reservoir['E10'],rate=0.7)
	p300.dispense(80, plate['E7'],rate=0.7)
	p300.aspirate(80, reservoir['E10'],rate=0.7)
	p300.dispense(80, plate['A2'],rate=0.7)
	p300.drop_tip()
	#Glucose_0_5
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['A5'],rate=0.7)
	p300.dispense(80, plate['D4'],rate=0.7)
	p300.aspirate(80, reservoir['A5'],rate=0.7)
	p300.dispense(80, plate['A3'],rate=0.7)
	p300.aspirate(80, reservoir['A5'],rate=0.7)
	p300.dispense(80, plate['B6'],rate=0.7)
	p300.aspirate(80, reservoir['A5'],rate=0.7)
	p300.dispense(80, plate['D7'],rate=0.7)
	p300.drop_tip()
	#NH4Cl_0_5
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['B2'],rate=0.7)
	p300.dispense(80, plate['D4'],rate=0.7)
	p300.aspirate(80, reservoir['B2'],rate=0.7)
	p300.dispense(80, plate['A3'],rate=0.7)
	p300.aspirate(80, reservoir['B2'],rate=0.7)
	p300.dispense(80, plate['B6'],rate=0.7)
	p300.aspirate(80, reservoir['B2'],rate=0.7)
	p300.dispense(80, plate['D7'],rate=0.7)
	p300.drop_tip()
	#MgSO4_0_5
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['B11'],rate=0.7)
	p300.dispense(80, plate['D4'],rate=0.7)
	p300.aspirate(80, reservoir['B11'],rate=0.7)
	p300.dispense(80, plate['A3'],rate=0.7)
	p300.aspirate(80, reservoir['B11'],rate=0.7)
	p300.dispense(80, plate['B6'],rate=0.7)
	p300.aspirate(80, reservoir['B11'],rate=0.7)
	p300.dispense(80, plate['D7'],rate=0.7)
	p300.drop_tip()
	#KH2PO4_0_5
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['C8'],rate=0.7)
	p300.dispense(80, plate['D4'],rate=0.7)
	p300.aspirate(80, reservoir['C8'],rate=0.7)
	p300.dispense(80, plate['A3'],rate=0.7)
	p300.aspirate(80, reservoir['C8'],rate=0.7)
	p300.dispense(80, plate['B6'],rate=0.7)
	p300.aspirate(80, reservoir['C8'],rate=0.7)
	p300.dispense(80, plate['D7'],rate=0.7)
	p300.drop_tip()
	#Na2HPO4_0_5
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['D5'],rate=0.7)
	p300.dispense(80, plate['D4'],rate=0.7)
	p300.aspirate(80, reservoir['D5'],rate=0.7)
	p300.dispense(80, plate['A3'],rate=0.7)
	p300.aspirate(80, reservoir['D5'],rate=0.7)
	p300.dispense(80, plate['B6'],rate=0.7)
	p300.aspirate(80, reservoir['D5'],rate=0.7)
	p300.dispense(80, plate['D7'],rate=0.7)
	p300.drop_tip()
	#CaCl2_0_5
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['E2'],rate=0.7)
	p300.dispense(80, plate['D4'],rate=0.7)
	p300.aspirate(80, reservoir['E2'],rate=0.7)
	p300.dispense(80, plate['A3'],rate=0.7)
	p300.aspirate(80, reservoir['E2'],rate=0.7)
	p300.dispense(80, plate['B6'],rate=0.7)
	p300.aspirate(80, reservoir['E2'],rate=0.7)
	p300.dispense(80, plate['D7'],rate=0.7)
	p300.drop_tip()
	#NaCl_0_5
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['E11'],rate=0.7)
	p300.dispense(80, plate['D4'],rate=0.7)
	p300.aspirate(80, reservoir['E11'],rate=0.7)
	p300.dispense(80, plate['A3'],rate=0.7)
	p300.aspirate(80, reservoir['E11'],rate=0.7)
	p300.dispense(80, plate['B6'],rate=0.7)
	p300.aspirate(80, reservoir['E11'],rate=0.7)
	p300.dispense(80, plate['D7'],rate=0.7)
	p300.drop_tip()
	#Glucose_0_6
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['A6'],rate=0.7)
	p300.dispense(80, plate['C3'],rate=0.7)
	p300.aspirate(80, reservoir['A6'],rate=0.7)
	p300.dispense(80, plate['D2'],rate=0.7)
	p300.aspirate(80, reservoir['A6'],rate=0.7)
	p300.dispense(80, plate['E5'],rate=0.7)
	p300.aspirate(80, reservoir['A6'],rate=0.7)
	p300.dispense(80, plate['C6'],rate=0.7)
	p300.drop_tip()
	#NH4Cl_0_6
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['B3'],rate=0.7)
	p300.dispense(80, plate['C3'],rate=0.7)
	p300.aspirate(80, reservoir['B3'],rate=0.7)
	p300.dispense(80, plate['D2'],rate=0.7)
	p300.aspirate(80, reservoir['B3'],rate=0.7)
	p300.dispense(80, plate['E5'],rate=0.7)
	p300.aspirate(80, reservoir['B3'],rate=0.7)
	p300.dispense(80, plate['C6'],rate=0.7)
	p300.drop_tip()
	#MgSO4_0_6
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['B12'],rate=0.7)
	p300.dispense(80, plate['C3'],rate=0.7)
	p300.aspirate(80, reservoir['B12'],rate=0.7)
	p300.dispense(80, plate['D2'],rate=0.7)
	p300.aspirate(80, reservoir['B12'],rate=0.7)
	p300.dispense(80, plate['E5'],rate=0.7)
	p300.aspirate(80, reservoir['B12'],rate=0.7)
	p300.dispense(80, plate['C6'],rate=0.7)
	p300.drop_tip()
	#KH2PO4_0_6
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['C9'],rate=0.7)
	p300.dispense(80, plate['C3'],rate=0.7)
	p300.aspirate(80, reservoir['C9'],rate=0.7)
	p300.dispense(80, plate['D2'],rate=0.7)
	p300.aspirate(80, reservoir['C9'],rate=0.7)
	p300.dispense(80, plate['E5'],rate=0.7)
	p300.aspirate(80, reservoir['C9'],rate=0.7)
	p300.dispense(80, plate['C6'],rate=0.7)
	p300.drop_tip()
	#Na2HPO4_0_6
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['D6'],rate=0.7)
	p300.dispense(80, plate['C3'],rate=0.7)
	p300.aspirate(80, reservoir['D6'],rate=0.7)
	p300.dispense(80, plate['D2'],rate=0.7)
	p300.aspirate(80, reservoir['D6'],rate=0.7)
	p300.dispense(80, plate['E5'],rate=0.7)
	p300.aspirate(80, reservoir['D6'],rate=0.7)
	p300.dispense(80, plate['C6'],rate=0.7)
	p300.drop_tip()
	#CaCl2_0_6
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['E3'],rate=0.7)
	p300.dispense(80, plate['C3'],rate=0.7)
	p300.aspirate(80, reservoir['E3'],rate=0.7)
	p300.dispense(80, plate['D2'],rate=0.7)
	p300.aspirate(80, reservoir['E3'],rate=0.7)
	p300.dispense(80, plate['E5'],rate=0.7)
	p300.aspirate(80, reservoir['E3'],rate=0.7)
	p300.dispense(80, plate['C6'],rate=0.7)
	p300.drop_tip()
	#NaCl_0_6
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['E12'],rate=0.7)
	p300.dispense(80, plate['C3'],rate=0.7)
	p300.aspirate(80, reservoir['E12'],rate=0.7)
	p300.dispense(80, plate['D2'],rate=0.7)
	p300.aspirate(80, reservoir['E12'],rate=0.7)
	p300.dispense(80, plate['E5'],rate=0.7)
	p300.aspirate(80, reservoir['E12'],rate=0.7)
	p300.dispense(80, plate['C6'],rate=0.7)
	p300.drop_tip()
	#Glucose_0_7
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['A7'],rate=0.7)
	p300.dispense(80, plate['A4'],rate=0.7)
	p300.aspirate(80, reservoir['A7'],rate=0.7)
	p300.dispense(80, plate['A5'],rate=0.7)
	p300.aspirate(80, reservoir['A7'],rate=0.7)
	p300.dispense(80, plate['F7'],rate=0.7)
	p300.aspirate(80, reservoir['A7'],rate=0.7)
	p300.dispense(80, plate['E2'],rate=0.7)
	p300.drop_tip()
	#NH4Cl_0_7
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['B4'],rate=0.7)
	p300.dispense(80, plate['A4'],rate=0.7)
	p300.aspirate(80, reservoir['B4'],rate=0.7)
	p300.dispense(80, plate['A5'],rate=0.7)
	p300.aspirate(80, reservoir['B4'],rate=0.7)
	p300.dispense(80, plate['F7'],rate=0.7)
	p300.aspirate(80, reservoir['B4'],rate=0.7)
	p300.dispense(80, plate['E2'],rate=0.7)
	p300.drop_tip()
	#MgSO4_0_7
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['C1'],rate=0.7)
	p300.dispense(80, plate['A4'],rate=0.7)
	p300.aspirate(80, reservoir['C1'],rate=0.7)
	p300.dispense(80, plate['A5'],rate=0.7)
	p300.aspirate(80, reservoir['C1'],rate=0.7)
	p300.dispense(80, plate['F7'],rate=0.7)
	p300.aspirate(80, reservoir['C1'],rate=0.7)
	p300.dispense(80, plate['E2'],rate=0.7)
	p300.drop_tip()
	#KH2PO4_0_7
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['C10'],rate=0.7)
	p300.dispense(80, plate['A4'],rate=0.7)
	p300.aspirate(80, reservoir['C10'],rate=0.7)
	p300.dispense(80, plate['A5'],rate=0.7)
	p300.aspirate(80, reservoir['C10'],rate=0.7)
	p300.dispense(80, plate['F7'],rate=0.7)
	p300.aspirate(80, reservoir['C10'],rate=0.7)
	p300.dispense(80, plate['E2'],rate=0.7)
	p300.drop_tip()
	#Na2HPO4_0_7
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['D7'],rate=0.7)
	p300.dispense(80, plate['A4'],rate=0.7)
	p300.aspirate(80, reservoir['D7'],rate=0.7)
	p300.dispense(80, plate['A5'],rate=0.7)
	p300.aspirate(80, reservoir['D7'],rate=0.7)
	p300.dispense(80, plate['F7'],rate=0.7)
	p300.aspirate(80, reservoir['D7'],rate=0.7)
	p300.dispense(80, plate['E2'],rate=0.7)
	p300.drop_tip()
	#CaCl2_0_7
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['E4'],rate=0.7)
	p300.dispense(80, plate['A4'],rate=0.7)
	p300.aspirate(80, reservoir['E4'],rate=0.7)
	p300.dispense(80, plate['A5'],rate=0.7)
	p300.aspirate(80, reservoir['E4'],rate=0.7)
	p300.dispense(80, plate['F7'],rate=0.7)
	p300.aspirate(80, reservoir['E4'],rate=0.7)
	p300.dispense(80, plate['E2'],rate=0.7)
	p300.drop_tip()
	#NaCl_0_7
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['F1'],rate=0.7)
	p300.dispense(80, plate['A4'],rate=0.7)
	p300.aspirate(80, reservoir['F1'],rate=0.7)
	p300.dispense(80, plate['A5'],rate=0.7)
	p300.aspirate(80, reservoir['F1'],rate=0.7)
	p300.dispense(80, plate['F7'],rate=0.7)
	p300.aspirate(80, reservoir['F1'],rate=0.7)
	p300.dispense(80, plate['E2'],rate=0.7)
	p300.drop_tip()
	#Glucose_0_CTRL
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['A8'],rate=0.7)
	p300.dispense(80, plate['F5'],rate=0.7)
	p300.aspirate(80, reservoir['A8'],rate=0.7)
	p300.dispense(80, plate['B3'],rate=0.7)
	p300.aspirate(80, reservoir['A8'],rate=0.7)
	p300.dispense(80, plate['E3'],rate=0.7)
	p300.aspirate(80, reservoir['A8'],rate=0.7)
	p300.dispense(80, plate['B7'],rate=0.7)
	p300.drop_tip()
	#NH4Cl_0_CTRL
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['B5'],rate=0.7)
	p300.dispense(80, plate['F5'],rate=0.7)
	p300.aspirate(80, reservoir['B5'],rate=0.7)
	p300.dispense(80, plate['B3'],rate=0.7)
	p300.aspirate(80, reservoir['B5'],rate=0.7)
	p300.dispense(80, plate['E3'],rate=0.7)
	p300.aspirate(80, reservoir['B5'],rate=0.7)
	p300.dispense(80, plate['B7'],rate=0.7)
	p300.drop_tip()
	#MgSO4_0_CTRL
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['C2'],rate=0.7)
	p300.dispense(80, plate['F5'],rate=0.7)
	p300.aspirate(80, reservoir['C2'],rate=0.7)
	p300.dispense(80, plate['B3'],rate=0.7)
	p300.aspirate(80, reservoir['C2'],rate=0.7)
	p300.dispense(80, plate['E3'],rate=0.7)
	p300.aspirate(80, reservoir['C2'],rate=0.7)
	p300.dispense(80, plate['B7'],rate=0.7)
	p300.drop_tip()
	#KH2PO4_0_CTRL
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['C11'],rate=0.7)
	p300.dispense(80, plate['F5'],rate=0.7)
	p300.aspirate(80, reservoir['C11'],rate=0.7)
	p300.dispense(80, plate['B3'],rate=0.7)
	p300.aspirate(80, reservoir['C11'],rate=0.7)
	p300.dispense(80, plate['E3'],rate=0.7)
	p300.aspirate(80, reservoir['C11'],rate=0.7)
	p300.dispense(80, plate['B7'],rate=0.7)
	p300.drop_tip()
	#Na2HPO4_0_CTRL
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['D8'],rate=0.7)
	p300.dispense(80, plate['F5'],rate=0.7)
	p300.aspirate(80, reservoir['D8'],rate=0.7)
	p300.dispense(80, plate['B3'],rate=0.7)
	p300.aspirate(80, reservoir['D8'],rate=0.7)
	p300.dispense(80, plate['E3'],rate=0.7)
	p300.aspirate(80, reservoir['D8'],rate=0.7)
	p300.dispense(80, plate['B7'],rate=0.7)
	p300.drop_tip()
	#CaCl2_0_CTRL
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['E5'],rate=0.7)
	p300.dispense(80, plate['F5'],rate=0.7)
	p300.aspirate(80, reservoir['E5'],rate=0.7)
	p300.dispense(80, plate['B3'],rate=0.7)
	p300.aspirate(80, reservoir['E5'],rate=0.7)
	p300.dispense(80, plate['E3'],rate=0.7)
	p300.aspirate(80, reservoir['E5'],rate=0.7)
	p300.dispense(80, plate['B7'],rate=0.7)
	p300.drop_tip()
	#NaCl_0_CTRL
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['F2'],rate=0.7)
	p300.dispense(80, plate['F5'],rate=0.7)
	p300.aspirate(80, reservoir['F2'],rate=0.7)
	p300.dispense(80, plate['B3'],rate=0.7)
	p300.aspirate(80, reservoir['F2'],rate=0.7)
	p300.dispense(80, plate['E3'],rate=0.7)
	p300.aspirate(80, reservoir['F2'],rate=0.7)
	p300.dispense(80, plate['B7'],rate=0.7)
	p300.drop_tip()
	#Glucose_0_REF
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['A9'],rate=0.7)
	p300.dispense(80, plate['C4'],rate=0.7)
	p300.aspirate(80, reservoir['A9'],rate=0.7)
	p300.dispense(80, plate['C7'],rate=0.7)
	p300.aspirate(80, reservoir['A9'],rate=0.7)
	p300.dispense(80, plate['E6'],rate=0.7)
	p300.aspirate(80, reservoir['A9'],rate=0.7)
	p300.dispense(80, plate['F2'],rate=0.7)
	p300.drop_tip()
	#NH4Cl_0_REF
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['B6'],rate=0.7)
	p300.dispense(80, plate['C4'],rate=0.7)
	p300.aspirate(80, reservoir['B6'],rate=0.7)
	p300.dispense(80, plate['C7'],rate=0.7)
	p300.aspirate(80, reservoir['B6'],rate=0.7)
	p300.dispense(80, plate['E6'],rate=0.7)
	p300.aspirate(80, reservoir['B6'],rate=0.7)
	p300.dispense(80, plate['F2'],rate=0.7)
	p300.drop_tip()
	#MgSO4_0_REF
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['C3'],rate=0.7)
	p300.dispense(80, plate['C4'],rate=0.7)
	p300.aspirate(80, reservoir['C3'],rate=0.7)
	p300.dispense(80, plate['C7'],rate=0.7)
	p300.aspirate(80, reservoir['C3'],rate=0.7)
	p300.dispense(80, plate['E6'],rate=0.7)
	p300.aspirate(80, reservoir['C3'],rate=0.7)
	p300.dispense(80, plate['F2'],rate=0.7)
	p300.drop_tip()
	#KH2PO4_0_REF
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['C12'],rate=0.7)
	p300.dispense(80, plate['C4'],rate=0.7)
	p300.aspirate(80, reservoir['C12'],rate=0.7)
	p300.dispense(80, plate['C7'],rate=0.7)
	p300.aspirate(80, reservoir['C12'],rate=0.7)
	p300.dispense(80, plate['E6'],rate=0.7)
	p300.aspirate(80, reservoir['C12'],rate=0.7)
	p300.dispense(80, plate['F2'],rate=0.7)
	p300.drop_tip()
	#Na2HPO4_0_REF
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['D9'],rate=0.7)
	p300.dispense(80, plate['C4'],rate=0.7)
	p300.aspirate(80, reservoir['D9'],rate=0.7)
	p300.dispense(80, plate['C7'],rate=0.7)
	p300.aspirate(80, reservoir['D9'],rate=0.7)
	p300.dispense(80, plate['E6'],rate=0.7)
	p300.aspirate(80, reservoir['D9'],rate=0.7)
	p300.dispense(80, plate['F2'],rate=0.7)
	p300.drop_tip()
	#CaCl2_0_REF
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['E6'],rate=0.7)
	p300.dispense(80, plate['C4'],rate=0.7)
	p300.aspirate(80, reservoir['E6'],rate=0.7)
	p300.dispense(80, plate['C7'],rate=0.7)
	p300.aspirate(80, reservoir['E6'],rate=0.7)
	p300.dispense(80, plate['E6'],rate=0.7)
	p300.aspirate(80, reservoir['E6'],rate=0.7)
	p300.dispense(80, plate['F2'],rate=0.7)
	p300.drop_tip()
	#NaCl_0_REF
	p300.pick_up_tip()
	p300.aspirate(80, reservoir['F3'],rate=0.7)
	p300.dispense(80, plate['C4'],rate=0.7)
	p300.aspirate(80, reservoir['F3'],rate=0.7)
	p300.dispense(80, plate['C7'],rate=0.7)
	p300.aspirate(80, reservoir['F3'],rate=0.7)
	p300.dispense(80, plate['E6'],rate=0.7)
	p300.aspirate(80, reservoir['F3'],rate=0.7)
	p300.dispense(80, plate['F2'],rate=0.7)
	p300.drop_tip()
	#water
	p300.pick_up_tip()
	p300.aspirate(160, big['A3'],rate=0.7)
	p300.dispense(160, plate['B4'],rate=0.7)
	p300.aspirate(160, big['A3'],rate=0.7)
	p300.dispense(160, plate['A7'],rate=0.7)
	p300.aspirate(160, big['A3'],rate=0.7)
	p300.dispense(160, plate['F4'],rate=0.7)
	p300.aspirate(160, big['A3'],rate=0.7)
	p300.dispense(160, plate['D5'],rate=0.7)
	p300.aspirate(160, big['A3'],rate=0.7)
	p300.dispense(160, plate['B2'],rate=0.7)
	p300.aspirate(160, big['A3'],rate=0.7)
	p300.dispense(160, plate['F6'],rate=0.7)
	p300.aspirate(160, big['A3'],rate=0.7)
	p300.dispense(160, plate['A6'],rate=0.7)
	p300.aspirate(160, big['A3'],rate=0.7)
	p300.dispense(160, plate['D3'],rate=0.7)
	p300.aspirate(160, big['A3'],rate=0.7)
	p300.dispense(160, plate['E4'],rate=0.7)
	p300.aspirate(160, big['A3'],rate=0.7)
	p300.dispense(160, plate['C2'],rate=0.7)
	p300.aspirate(160, big['A3'],rate=0.7)
	p300.dispense(160, plate['B5'],rate=0.7)
	p300.aspirate(160, big['A3'],rate=0.7)
	p300.dispense(160, plate['D6'],rate=0.7)
	p300.aspirate(160, big['A3'],rate=0.7)
	p300.dispense(160, plate['C5'],rate=0.7)
	p300.aspirate(160, big['A3'],rate=0.7)
	p300.dispense(160, plate['F3'],rate=0.7)
	p300.aspirate(160, big['A3'],rate=0.7)
	p300.dispense(160, plate['E7'],rate=0.7)
	p300.aspirate(160, big['A3'],rate=0.7)
	p300.dispense(160, plate['A2'],rate=0.7)
	p300.aspirate(160, big['A3'],rate=0.7)
	p300.dispense(160, plate['D4'],rate=0.7)
	p300.aspirate(160, big['A3'],rate=0.7)
	p300.dispense(160, plate['A3'],rate=0.7)
	p300.aspirate(160, big['A3'],rate=0.7)
	p300.dispense(160, plate['B6'],rate=0.7)
	p300.aspirate(160, big['A3'],rate=0.7)
	p300.dispense(160, plate['D7'],rate=0.7)
	p300.aspirate(160, big['A3'],rate=0.7)
	p300.dispense(160, plate['C3'],rate=0.7)
	p300.aspirate(160, big['A3'],rate=0.7)
	p300.dispense(160, plate['D2'],rate=0.7)
	p300.aspirate(160, big['A3'],rate=0.7)
	p300.dispense(160, plate['E5'],rate=0.7)
	p300.aspirate(160, big['A3'],rate=0.7)
	p300.dispense(160, plate['C6'],rate=0.7)
	p300.aspirate(160, big['A3'],rate=0.7)
	p300.dispense(160, plate['A4'],rate=0.7)
	p300.aspirate(160, big['A3'],rate=0.7)
	p300.dispense(160, plate['A5'],rate=0.7)
	p300.aspirate(160, big['A3'],rate=0.7)
	p300.dispense(160, plate['F7'],rate=0.7)
	p300.aspirate(160, big['A3'],rate=0.7)
	p300.dispense(160, plate['E2'],rate=0.7)
	p300.aspirate(160, big['A3'],rate=0.7)
	p300.dispense(160, plate['F5'],rate=0.7)
	p300.aspirate(160, big['A3'],rate=0.7)
	p300.dispense(160, plate['B3'],rate=0.7)
	p300.aspirate(160, big['A3'],rate=0.7)
	p300.dispense(160, plate['E3'],rate=0.7)
	p300.aspirate(160, big['A3'],rate=0.7)
	p300.dispense(160, plate['B7'],rate=0.7)
	p300.aspirate(160, big['A3'],rate=0.7)
	p300.dispense(160, plate['C4'],rate=0.7)
	p300.aspirate(160, big['A3'],rate=0.7)
	p300.dispense(160, plate['C7'],rate=0.7)
	p300.aspirate(160, big['A3'],rate=0.7)
	p300.dispense(160, plate['E6'],rate=0.7)
	p300.aspirate(160, big['A3'],rate=0.7)
	p300.dispense(160, plate['F2'],rate=0.7)
	p300.drop_tip()
