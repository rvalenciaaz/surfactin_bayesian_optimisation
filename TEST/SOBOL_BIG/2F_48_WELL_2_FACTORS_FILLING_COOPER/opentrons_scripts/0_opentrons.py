from opentrons import protocol_api
metadata = {'apiLevel': '2.13'}
def run(protocol: protocol_api.ProtocolContext):
	plate = protocol.load_labware('corning_48_wellplate_1.6ml_flat', 8)
	tiprack_2 = protocol.load_labware('opentrons_96_tiprack_300ul', 11)
	reservoir_1= protocol.load_labware('opentrons_24_tuberack_eppendorf_2ml_safelock_snapcap',1)
	reservoir_2= protocol.load_labware('opentrons_24_tuberack_eppendorf_2ml_safelock_snapcap',2)
	reservoir_3= protocol.load_labware('opentrons_24_tuberack_eppendorf_2ml_safelock_snapcap',3)
	reservoir_4= protocol.load_labware('opentrons_24_tuberack_eppendorf_2ml_safelock_snapcap',4)
	reservoir_5= protocol.load_labware('opentrons_24_tuberack_eppendorf_2ml_safelock_snapcap',5)
	big= protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical',6)
	p300 = protocol.load_instrument('p300_single', 'left', tip_racks=[tiprack_2])
	#Glucose_0_1
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_1['A1'],rate=0.7)
	p300.dispense(80, plate['E7'],rate=0.7)
	p300.aspirate(80, reservoir_1['A1'],rate=0.7)
	p300.dispense(80, plate['B3'],rate=0.7)
	p300.aspirate(80, reservoir_1['A1'],rate=0.7)
	p300.dispense(80, plate['D3'],rate=0.7)
	p300.aspirate(80, reservoir_1['A1'],rate=0.7)
	p300.dispense(80, plate['A5'],rate=0.7)
	p300.drop_tip()
	#NH4NO3_0_1
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_1['C1'],rate=0.7)
	p300.dispense(80, plate['E7'],rate=0.7)
	p300.aspirate(80, reservoir_1['C1'],rate=0.7)
	p300.dispense(80, plate['B3'],rate=0.7)
	p300.aspirate(80, reservoir_1['C1'],rate=0.7)
	p300.dispense(80, plate['D3'],rate=0.7)
	p300.aspirate(80, reservoir_1['C1'],rate=0.7)
	p300.dispense(80, plate['A5'],rate=0.7)
	p300.drop_tip()
	#MgSO4_0_1
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_2['A1'],rate=0.7)
	p300.dispense(80, plate['E7'],rate=0.7)
	p300.aspirate(80, reservoir_2['A1'],rate=0.7)
	p300.dispense(80, plate['B3'],rate=0.7)
	p300.aspirate(80, reservoir_2['A1'],rate=0.7)
	p300.dispense(80, plate['D3'],rate=0.7)
	p300.aspirate(80, reservoir_2['A1'],rate=0.7)
	p300.dispense(80, plate['A5'],rate=0.7)
	p300.drop_tip()
	#KH2PO4_0_1
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_2['C1'],rate=0.7)
	p300.dispense(80, plate['E7'],rate=0.7)
	p300.aspirate(80, reservoir_2['C1'],rate=0.7)
	p300.dispense(80, plate['B3'],rate=0.7)
	p300.aspirate(80, reservoir_2['C1'],rate=0.7)
	p300.dispense(80, plate['D3'],rate=0.7)
	p300.aspirate(80, reservoir_2['C1'],rate=0.7)
	p300.dispense(80, plate['A5'],rate=0.7)
	p300.drop_tip()
	#Na2HPO4_0_1
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_3['A1'],rate=0.7)
	p300.dispense(80, plate['E7'],rate=0.7)
	p300.aspirate(80, reservoir_3['A1'],rate=0.7)
	p300.dispense(80, plate['B3'],rate=0.7)
	p300.aspirate(80, reservoir_3['A1'],rate=0.7)
	p300.dispense(80, plate['D3'],rate=0.7)
	p300.aspirate(80, reservoir_3['A1'],rate=0.7)
	p300.dispense(80, plate['A5'],rate=0.7)
	p300.drop_tip()
	#Na2EDTA_0_1
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_3['C1'],rate=0.7)
	p300.dispense(80, plate['E7'],rate=0.7)
	p300.aspirate(80, reservoir_3['C1'],rate=0.7)
	p300.dispense(80, plate['B3'],rate=0.7)
	p300.aspirate(80, reservoir_3['C1'],rate=0.7)
	p300.dispense(80, plate['D3'],rate=0.7)
	p300.aspirate(80, reservoir_3['C1'],rate=0.7)
	p300.dispense(80, plate['A5'],rate=0.7)
	p300.drop_tip()
	#CaCl2_0_1
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_4['A1'],rate=0.7)
	p300.dispense(80, plate['E7'],rate=0.7)
	p300.aspirate(80, reservoir_4['A1'],rate=0.7)
	p300.dispense(80, plate['B3'],rate=0.7)
	p300.aspirate(80, reservoir_4['A1'],rate=0.7)
	p300.dispense(80, plate['D3'],rate=0.7)
	p300.aspirate(80, reservoir_4['A1'],rate=0.7)
	p300.dispense(80, plate['A5'],rate=0.7)
	p300.drop_tip()
	#FeSO4_0_1
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_4['C1'],rate=0.7)
	p300.dispense(80, plate['E7'],rate=0.7)
	p300.aspirate(80, reservoir_4['C1'],rate=0.7)
	p300.dispense(80, plate['B3'],rate=0.7)
	p300.aspirate(80, reservoir_4['C1'],rate=0.7)
	p300.dispense(80, plate['D3'],rate=0.7)
	p300.aspirate(80, reservoir_4['C1'],rate=0.7)
	p300.dispense(80, plate['A5'],rate=0.7)
	p300.drop_tip()
	#MnSO4_0_1
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_5['A1'],rate=0.7)
	p300.dispense(80, plate['E7'],rate=0.7)
	p300.aspirate(80, reservoir_5['A1'],rate=0.7)
	p300.dispense(80, plate['B3'],rate=0.7)
	p300.aspirate(80, reservoir_5['A1'],rate=0.7)
	p300.dispense(80, plate['D3'],rate=0.7)
	p300.aspirate(80, reservoir_5['A1'],rate=0.7)
	p300.dispense(80, plate['A5'],rate=0.7)
	p300.drop_tip()
	#Glucose_0_2
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_1['A2'],rate=0.7)
	p300.dispense(80, plate['B2'],rate=0.7)
	p300.aspirate(80, reservoir_1['A2'],rate=0.7)
	p300.dispense(80, plate['E5'],rate=0.7)
	p300.aspirate(80, reservoir_1['A2'],rate=0.7)
	p300.dispense(80, plate['E3'],rate=0.7)
	p300.aspirate(80, reservoir_1['A2'],rate=0.7)
	p300.dispense(80, plate['A6'],rate=0.7)
	p300.drop_tip()
	#NH4NO3_0_2
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_1['C2'],rate=0.7)
	p300.dispense(80, plate['B2'],rate=0.7)
	p300.aspirate(80, reservoir_1['C2'],rate=0.7)
	p300.dispense(80, plate['E5'],rate=0.7)
	p300.aspirate(80, reservoir_1['C2'],rate=0.7)
	p300.dispense(80, plate['E3'],rate=0.7)
	p300.aspirate(80, reservoir_1['C2'],rate=0.7)
	p300.dispense(80, plate['A6'],rate=0.7)
	p300.drop_tip()
	#MgSO4_0_2
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_2['A2'],rate=0.7)
	p300.dispense(80, plate['B2'],rate=0.7)
	p300.aspirate(80, reservoir_2['A2'],rate=0.7)
	p300.dispense(80, plate['E5'],rate=0.7)
	p300.aspirate(80, reservoir_2['A2'],rate=0.7)
	p300.dispense(80, plate['E3'],rate=0.7)
	p300.aspirate(80, reservoir_2['A2'],rate=0.7)
	p300.dispense(80, plate['A6'],rate=0.7)
	p300.drop_tip()
	#KH2PO4_0_2
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_2['C2'],rate=0.7)
	p300.dispense(80, plate['B2'],rate=0.7)
	p300.aspirate(80, reservoir_2['C2'],rate=0.7)
	p300.dispense(80, plate['E5'],rate=0.7)
	p300.aspirate(80, reservoir_2['C2'],rate=0.7)
	p300.dispense(80, plate['E3'],rate=0.7)
	p300.aspirate(80, reservoir_2['C2'],rate=0.7)
	p300.dispense(80, plate['A6'],rate=0.7)
	p300.drop_tip()
	#Na2HPO4_0_2
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_3['A2'],rate=0.7)
	p300.dispense(80, plate['B2'],rate=0.7)
	p300.aspirate(80, reservoir_3['A2'],rate=0.7)
	p300.dispense(80, plate['E5'],rate=0.7)
	p300.aspirate(80, reservoir_3['A2'],rate=0.7)
	p300.dispense(80, plate['E3'],rate=0.7)
	p300.aspirate(80, reservoir_3['A2'],rate=0.7)
	p300.dispense(80, plate['A6'],rate=0.7)
	p300.drop_tip()
	#Na2EDTA_0_2
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_3['C2'],rate=0.7)
	p300.dispense(80, plate['B2'],rate=0.7)
	p300.aspirate(80, reservoir_3['C2'],rate=0.7)
	p300.dispense(80, plate['E5'],rate=0.7)
	p300.aspirate(80, reservoir_3['C2'],rate=0.7)
	p300.dispense(80, plate['E3'],rate=0.7)
	p300.aspirate(80, reservoir_3['C2'],rate=0.7)
	p300.dispense(80, plate['A6'],rate=0.7)
	p300.drop_tip()
	#CaCl2_0_2
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_4['A2'],rate=0.7)
	p300.dispense(80, plate['B2'],rate=0.7)
	p300.aspirate(80, reservoir_4['A2'],rate=0.7)
	p300.dispense(80, plate['E5'],rate=0.7)
	p300.aspirate(80, reservoir_4['A2'],rate=0.7)
	p300.dispense(80, plate['E3'],rate=0.7)
	p300.aspirate(80, reservoir_4['A2'],rate=0.7)
	p300.dispense(80, plate['A6'],rate=0.7)
	p300.drop_tip()
	#FeSO4_0_2
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_4['C2'],rate=0.7)
	p300.dispense(80, plate['B2'],rate=0.7)
	p300.aspirate(80, reservoir_4['C2'],rate=0.7)
	p300.dispense(80, plate['E5'],rate=0.7)
	p300.aspirate(80, reservoir_4['C2'],rate=0.7)
	p300.dispense(80, plate['E3'],rate=0.7)
	p300.aspirate(80, reservoir_4['C2'],rate=0.7)
	p300.dispense(80, plate['A6'],rate=0.7)
	p300.drop_tip()
	#MnSO4_0_2
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_5['A2'],rate=0.7)
	p300.dispense(80, plate['B2'],rate=0.7)
	p300.aspirate(80, reservoir_5['A2'],rate=0.7)
	p300.dispense(80, plate['E5'],rate=0.7)
	p300.aspirate(80, reservoir_5['A2'],rate=0.7)
	p300.dispense(80, plate['E3'],rate=0.7)
	p300.aspirate(80, reservoir_5['A2'],rate=0.7)
	p300.dispense(80, plate['A6'],rate=0.7)
	p300.drop_tip()
	#Glucose_0_3
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_1['A3'],rate=0.7)
	p300.dispense(80, plate['F4'],rate=0.7)
	p300.aspirate(80, reservoir_1['A3'],rate=0.7)
	p300.dispense(80, plate['C5'],rate=0.7)
	p300.aspirate(80, reservoir_1['A3'],rate=0.7)
	p300.dispense(80, plate['F7'],rate=0.7)
	p300.aspirate(80, reservoir_1['A3'],rate=0.7)
	p300.dispense(80, plate['A4'],rate=0.7)
	p300.drop_tip()
	#NH4NO3_0_3
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_1['C3'],rate=0.7)
	p300.dispense(80, plate['F4'],rate=0.7)
	p300.aspirate(80, reservoir_1['C3'],rate=0.7)
	p300.dispense(80, plate['C5'],rate=0.7)
	p300.aspirate(80, reservoir_1['C3'],rate=0.7)
	p300.dispense(80, plate['F7'],rate=0.7)
	p300.aspirate(80, reservoir_1['C3'],rate=0.7)
	p300.dispense(80, plate['A4'],rate=0.7)
	p300.drop_tip()
	#MgSO4_0_3
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_2['A3'],rate=0.7)
	p300.dispense(80, plate['F4'],rate=0.7)
	p300.aspirate(80, reservoir_2['A3'],rate=0.7)
	p300.dispense(80, plate['C5'],rate=0.7)
	p300.aspirate(80, reservoir_2['A3'],rate=0.7)
	p300.dispense(80, plate['F7'],rate=0.7)
	p300.aspirate(80, reservoir_2['A3'],rate=0.7)
	p300.dispense(80, plate['A4'],rate=0.7)
	p300.drop_tip()
	#KH2PO4_0_3
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_2['C3'],rate=0.7)
	p300.dispense(80, plate['F4'],rate=0.7)
	p300.aspirate(80, reservoir_2['C3'],rate=0.7)
	p300.dispense(80, plate['C5'],rate=0.7)
	p300.aspirate(80, reservoir_2['C3'],rate=0.7)
	p300.dispense(80, plate['F7'],rate=0.7)
	p300.aspirate(80, reservoir_2['C3'],rate=0.7)
	p300.dispense(80, plate['A4'],rate=0.7)
	p300.drop_tip()
	#Na2HPO4_0_3
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_3['A3'],rate=0.7)
	p300.dispense(80, plate['F4'],rate=0.7)
	p300.aspirate(80, reservoir_3['A3'],rate=0.7)
	p300.dispense(80, plate['C5'],rate=0.7)
	p300.aspirate(80, reservoir_3['A3'],rate=0.7)
	p300.dispense(80, plate['F7'],rate=0.7)
	p300.aspirate(80, reservoir_3['A3'],rate=0.7)
	p300.dispense(80, plate['A4'],rate=0.7)
	p300.drop_tip()
	#Na2EDTA_0_3
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_3['C3'],rate=0.7)
	p300.dispense(80, plate['F4'],rate=0.7)
	p300.aspirate(80, reservoir_3['C3'],rate=0.7)
	p300.dispense(80, plate['C5'],rate=0.7)
	p300.aspirate(80, reservoir_3['C3'],rate=0.7)
	p300.dispense(80, plate['F7'],rate=0.7)
	p300.aspirate(80, reservoir_3['C3'],rate=0.7)
	p300.dispense(80, plate['A4'],rate=0.7)
	p300.drop_tip()
	#CaCl2_0_3
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_4['A3'],rate=0.7)
	p300.dispense(80, plate['F4'],rate=0.7)
	p300.aspirate(80, reservoir_4['A3'],rate=0.7)
	p300.dispense(80, plate['C5'],rate=0.7)
	p300.aspirate(80, reservoir_4['A3'],rate=0.7)
	p300.dispense(80, plate['F7'],rate=0.7)
	p300.aspirate(80, reservoir_4['A3'],rate=0.7)
	p300.dispense(80, plate['A4'],rate=0.7)
	p300.drop_tip()
	#FeSO4_0_3
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_4['C3'],rate=0.7)
	p300.dispense(80, plate['F4'],rate=0.7)
	p300.aspirate(80, reservoir_4['C3'],rate=0.7)
	p300.dispense(80, plate['C5'],rate=0.7)
	p300.aspirate(80, reservoir_4['C3'],rate=0.7)
	p300.dispense(80, plate['F7'],rate=0.7)
	p300.aspirate(80, reservoir_4['C3'],rate=0.7)
	p300.dispense(80, plate['A4'],rate=0.7)
	p300.drop_tip()
	#MnSO4_0_3
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_5['A3'],rate=0.7)
	p300.dispense(80, plate['F4'],rate=0.7)
	p300.aspirate(80, reservoir_5['A3'],rate=0.7)
	p300.dispense(80, plate['C5'],rate=0.7)
	p300.aspirate(80, reservoir_5['A3'],rate=0.7)
	p300.dispense(80, plate['F7'],rate=0.7)
	p300.aspirate(80, reservoir_5['A3'],rate=0.7)
	p300.dispense(80, plate['A4'],rate=0.7)
	p300.drop_tip()
	#Glucose_0_4
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_1['A4'],rate=0.7)
	p300.dispense(80, plate['D6'],rate=0.7)
	p300.aspirate(80, reservoir_1['A4'],rate=0.7)
	p300.dispense(80, plate['C6'],rate=0.7)
	p300.aspirate(80, reservoir_1['A4'],rate=0.7)
	p300.dispense(80, plate['E4'],rate=0.7)
	p300.aspirate(80, reservoir_1['A4'],rate=0.7)
	p300.dispense(80, plate['C2'],rate=0.7)
	p300.drop_tip()
	#NH4NO3_0_4
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_1['C4'],rate=0.7)
	p300.dispense(80, plate['D6'],rate=0.7)
	p300.aspirate(80, reservoir_1['C4'],rate=0.7)
	p300.dispense(80, plate['C6'],rate=0.7)
	p300.aspirate(80, reservoir_1['C4'],rate=0.7)
	p300.dispense(80, plate['E4'],rate=0.7)
	p300.aspirate(80, reservoir_1['C4'],rate=0.7)
	p300.dispense(80, plate['C2'],rate=0.7)
	p300.drop_tip()
	#MgSO4_0_4
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_2['A4'],rate=0.7)
	p300.dispense(80, plate['D6'],rate=0.7)
	p300.aspirate(80, reservoir_2['A4'],rate=0.7)
	p300.dispense(80, plate['C6'],rate=0.7)
	p300.aspirate(80, reservoir_2['A4'],rate=0.7)
	p300.dispense(80, plate['E4'],rate=0.7)
	p300.aspirate(80, reservoir_2['A4'],rate=0.7)
	p300.dispense(80, plate['C2'],rate=0.7)
	p300.drop_tip()
	#KH2PO4_0_4
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_2['C4'],rate=0.7)
	p300.dispense(80, plate['D6'],rate=0.7)
	p300.aspirate(80, reservoir_2['C4'],rate=0.7)
	p300.dispense(80, plate['C6'],rate=0.7)
	p300.aspirate(80, reservoir_2['C4'],rate=0.7)
	p300.dispense(80, plate['E4'],rate=0.7)
	p300.aspirate(80, reservoir_2['C4'],rate=0.7)
	p300.dispense(80, plate['C2'],rate=0.7)
	p300.drop_tip()
	#Na2HPO4_0_4
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_3['A4'],rate=0.7)
	p300.dispense(80, plate['D6'],rate=0.7)
	p300.aspirate(80, reservoir_3['A4'],rate=0.7)
	p300.dispense(80, plate['C6'],rate=0.7)
	p300.aspirate(80, reservoir_3['A4'],rate=0.7)
	p300.dispense(80, plate['E4'],rate=0.7)
	p300.aspirate(80, reservoir_3['A4'],rate=0.7)
	p300.dispense(80, plate['C2'],rate=0.7)
	p300.drop_tip()
	#Na2EDTA_0_4
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_3['C4'],rate=0.7)
	p300.dispense(80, plate['D6'],rate=0.7)
	p300.aspirate(80, reservoir_3['C4'],rate=0.7)
	p300.dispense(80, plate['C6'],rate=0.7)
	p300.aspirate(80, reservoir_3['C4'],rate=0.7)
	p300.dispense(80, plate['E4'],rate=0.7)
	p300.aspirate(80, reservoir_3['C4'],rate=0.7)
	p300.dispense(80, plate['C2'],rate=0.7)
	p300.drop_tip()
	#CaCl2_0_4
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_4['A4'],rate=0.7)
	p300.dispense(80, plate['D6'],rate=0.7)
	p300.aspirate(80, reservoir_4['A4'],rate=0.7)
	p300.dispense(80, plate['C6'],rate=0.7)
	p300.aspirate(80, reservoir_4['A4'],rate=0.7)
	p300.dispense(80, plate['E4'],rate=0.7)
	p300.aspirate(80, reservoir_4['A4'],rate=0.7)
	p300.dispense(80, plate['C2'],rate=0.7)
	p300.drop_tip()
	#FeSO4_0_4
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_4['C4'],rate=0.7)
	p300.dispense(80, plate['D6'],rate=0.7)
	p300.aspirate(80, reservoir_4['C4'],rate=0.7)
	p300.dispense(80, plate['C6'],rate=0.7)
	p300.aspirate(80, reservoir_4['C4'],rate=0.7)
	p300.dispense(80, plate['E4'],rate=0.7)
	p300.aspirate(80, reservoir_4['C4'],rate=0.7)
	p300.dispense(80, plate['C2'],rate=0.7)
	p300.drop_tip()
	#MnSO4_0_4
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_5['A4'],rate=0.7)
	p300.dispense(80, plate['D6'],rate=0.7)
	p300.aspirate(80, reservoir_5['A4'],rate=0.7)
	p300.dispense(80, plate['C6'],rate=0.7)
	p300.aspirate(80, reservoir_5['A4'],rate=0.7)
	p300.dispense(80, plate['E4'],rate=0.7)
	p300.aspirate(80, reservoir_5['A4'],rate=0.7)
	p300.dispense(80, plate['C2'],rate=0.7)
	p300.drop_tip()
	#Glucose_0_5
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_1['A5'],rate=0.7)
	p300.dispense(80, plate['D2'],rate=0.7)
	p300.aspirate(80, reservoir_1['A5'],rate=0.7)
	p300.dispense(80, plate['A7'],rate=0.7)
	p300.aspirate(80, reservoir_1['A5'],rate=0.7)
	p300.dispense(80, plate['C3'],rate=0.7)
	p300.aspirate(80, reservoir_1['A5'],rate=0.7)
	p300.dispense(80, plate['D5'],rate=0.7)
	p300.drop_tip()
	#NH4NO3_0_5
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_1['C5'],rate=0.7)
	p300.dispense(80, plate['D2'],rate=0.7)
	p300.aspirate(80, reservoir_1['C5'],rate=0.7)
	p300.dispense(80, plate['A7'],rate=0.7)
	p300.aspirate(80, reservoir_1['C5'],rate=0.7)
	p300.dispense(80, plate['C3'],rate=0.7)
	p300.aspirate(80, reservoir_1['C5'],rate=0.7)
	p300.dispense(80, plate['D5'],rate=0.7)
	p300.drop_tip()
	#MgSO4_0_5
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_2['A5'],rate=0.7)
	p300.dispense(80, plate['D2'],rate=0.7)
	p300.aspirate(80, reservoir_2['A5'],rate=0.7)
	p300.dispense(80, plate['A7'],rate=0.7)
	p300.aspirate(80, reservoir_2['A5'],rate=0.7)
	p300.dispense(80, plate['C3'],rate=0.7)
	p300.aspirate(80, reservoir_2['A5'],rate=0.7)
	p300.dispense(80, plate['D5'],rate=0.7)
	p300.drop_tip()
	#KH2PO4_0_5
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_2['C5'],rate=0.7)
	p300.dispense(80, plate['D2'],rate=0.7)
	p300.aspirate(80, reservoir_2['C5'],rate=0.7)
	p300.dispense(80, plate['A7'],rate=0.7)
	p300.aspirate(80, reservoir_2['C5'],rate=0.7)
	p300.dispense(80, plate['C3'],rate=0.7)
	p300.aspirate(80, reservoir_2['C5'],rate=0.7)
	p300.dispense(80, plate['D5'],rate=0.7)
	p300.drop_tip()
	#Na2HPO4_0_5
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_3['A5'],rate=0.7)
	p300.dispense(80, plate['D2'],rate=0.7)
	p300.aspirate(80, reservoir_3['A5'],rate=0.7)
	p300.dispense(80, plate['A7'],rate=0.7)
	p300.aspirate(80, reservoir_3['A5'],rate=0.7)
	p300.dispense(80, plate['C3'],rate=0.7)
	p300.aspirate(80, reservoir_3['A5'],rate=0.7)
	p300.dispense(80, plate['D5'],rate=0.7)
	p300.drop_tip()
	#Na2EDTA_0_5
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_3['C5'],rate=0.7)
	p300.dispense(80, plate['D2'],rate=0.7)
	p300.aspirate(80, reservoir_3['C5'],rate=0.7)
	p300.dispense(80, plate['A7'],rate=0.7)
	p300.aspirate(80, reservoir_3['C5'],rate=0.7)
	p300.dispense(80, plate['C3'],rate=0.7)
	p300.aspirate(80, reservoir_3['C5'],rate=0.7)
	p300.dispense(80, plate['D5'],rate=0.7)
	p300.drop_tip()
	#CaCl2_0_5
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_4['A5'],rate=0.7)
	p300.dispense(80, plate['D2'],rate=0.7)
	p300.aspirate(80, reservoir_4['A5'],rate=0.7)
	p300.dispense(80, plate['A7'],rate=0.7)
	p300.aspirate(80, reservoir_4['A5'],rate=0.7)
	p300.dispense(80, plate['C3'],rate=0.7)
	p300.aspirate(80, reservoir_4['A5'],rate=0.7)
	p300.dispense(80, plate['D5'],rate=0.7)
	p300.drop_tip()
	#FeSO4_0_5
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_4['C5'],rate=0.7)
	p300.dispense(80, plate['D2'],rate=0.7)
	p300.aspirate(80, reservoir_4['C5'],rate=0.7)
	p300.dispense(80, plate['A7'],rate=0.7)
	p300.aspirate(80, reservoir_4['C5'],rate=0.7)
	p300.dispense(80, plate['C3'],rate=0.7)
	p300.aspirate(80, reservoir_4['C5'],rate=0.7)
	p300.dispense(80, plate['D5'],rate=0.7)
	p300.drop_tip()
	#MnSO4_0_5
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_5['A5'],rate=0.7)
	p300.dispense(80, plate['D2'],rate=0.7)
	p300.aspirate(80, reservoir_5['A5'],rate=0.7)
	p300.dispense(80, plate['A7'],rate=0.7)
	p300.aspirate(80, reservoir_5['A5'],rate=0.7)
	p300.dispense(80, plate['C3'],rate=0.7)
	p300.aspirate(80, reservoir_5['A5'],rate=0.7)
	p300.dispense(80, plate['D5'],rate=0.7)
	p300.drop_tip()
	#Glucose_0_6
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_1['A6'],rate=0.7)
	p300.dispense(80, plate['A2'],rate=0.7)
	p300.aspirate(80, reservoir_1['A6'],rate=0.7)
	p300.dispense(80, plate['E2'],rate=0.7)
	p300.aspirate(80, reservoir_1['A6'],rate=0.7)
	p300.dispense(80, plate['B7'],rate=0.7)
	p300.aspirate(80, reservoir_1['A6'],rate=0.7)
	p300.dispense(80, plate['D7'],rate=0.7)
	p300.drop_tip()
	#NH4NO3_0_6
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_1['C6'],rate=0.7)
	p300.dispense(80, plate['A2'],rate=0.7)
	p300.aspirate(80, reservoir_1['C6'],rate=0.7)
	p300.dispense(80, plate['E2'],rate=0.7)
	p300.aspirate(80, reservoir_1['C6'],rate=0.7)
	p300.dispense(80, plate['B7'],rate=0.7)
	p300.aspirate(80, reservoir_1['C6'],rate=0.7)
	p300.dispense(80, plate['D7'],rate=0.7)
	p300.drop_tip()
	#MgSO4_0_6
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_2['A6'],rate=0.7)
	p300.dispense(80, plate['A2'],rate=0.7)
	p300.aspirate(80, reservoir_2['A6'],rate=0.7)
	p300.dispense(80, plate['E2'],rate=0.7)
	p300.aspirate(80, reservoir_2['A6'],rate=0.7)
	p300.dispense(80, plate['B7'],rate=0.7)
	p300.aspirate(80, reservoir_2['A6'],rate=0.7)
	p300.dispense(80, plate['D7'],rate=0.7)
	p300.drop_tip()
	#KH2PO4_0_6
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_2['C6'],rate=0.7)
	p300.dispense(80, plate['A2'],rate=0.7)
	p300.aspirate(80, reservoir_2['C6'],rate=0.7)
	p300.dispense(80, plate['E2'],rate=0.7)
	p300.aspirate(80, reservoir_2['C6'],rate=0.7)
	p300.dispense(80, plate['B7'],rate=0.7)
	p300.aspirate(80, reservoir_2['C6'],rate=0.7)
	p300.dispense(80, plate['D7'],rate=0.7)
	p300.drop_tip()
	#Na2HPO4_0_6
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_3['A6'],rate=0.7)
	p300.dispense(80, plate['A2'],rate=0.7)
	p300.aspirate(80, reservoir_3['A6'],rate=0.7)
	p300.dispense(80, plate['E2'],rate=0.7)
	p300.aspirate(80, reservoir_3['A6'],rate=0.7)
	p300.dispense(80, plate['B7'],rate=0.7)
	p300.aspirate(80, reservoir_3['A6'],rate=0.7)
	p300.dispense(80, plate['D7'],rate=0.7)
	p300.drop_tip()
	#Na2EDTA_0_6
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_3['C6'],rate=0.7)
	p300.dispense(80, plate['A2'],rate=0.7)
	p300.aspirate(80, reservoir_3['C6'],rate=0.7)
	p300.dispense(80, plate['E2'],rate=0.7)
	p300.aspirate(80, reservoir_3['C6'],rate=0.7)
	p300.dispense(80, plate['B7'],rate=0.7)
	p300.aspirate(80, reservoir_3['C6'],rate=0.7)
	p300.dispense(80, plate['D7'],rate=0.7)
	p300.drop_tip()
	#CaCl2_0_6
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_4['A6'],rate=0.7)
	p300.dispense(80, plate['A2'],rate=0.7)
	p300.aspirate(80, reservoir_4['A6'],rate=0.7)
	p300.dispense(80, plate['E2'],rate=0.7)
	p300.aspirate(80, reservoir_4['A6'],rate=0.7)
	p300.dispense(80, plate['B7'],rate=0.7)
	p300.aspirate(80, reservoir_4['A6'],rate=0.7)
	p300.dispense(80, plate['D7'],rate=0.7)
	p300.drop_tip()
	#FeSO4_0_6
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_4['C6'],rate=0.7)
	p300.dispense(80, plate['A2'],rate=0.7)
	p300.aspirate(80, reservoir_4['C6'],rate=0.7)
	p300.dispense(80, plate['E2'],rate=0.7)
	p300.aspirate(80, reservoir_4['C6'],rate=0.7)
	p300.dispense(80, plate['B7'],rate=0.7)
	p300.aspirate(80, reservoir_4['C6'],rate=0.7)
	p300.dispense(80, plate['D7'],rate=0.7)
	p300.drop_tip()
	#MnSO4_0_6
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_5['A6'],rate=0.7)
	p300.dispense(80, plate['A2'],rate=0.7)
	p300.aspirate(80, reservoir_5['A6'],rate=0.7)
	p300.dispense(80, plate['E2'],rate=0.7)
	p300.aspirate(80, reservoir_5['A6'],rate=0.7)
	p300.dispense(80, plate['B7'],rate=0.7)
	p300.aspirate(80, reservoir_5['A6'],rate=0.7)
	p300.dispense(80, plate['D7'],rate=0.7)
	p300.drop_tip()
	#Glucose_0_7
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_1['B1'],rate=0.7)
	p300.dispense(80, plate['F2'],rate=0.7)
	p300.aspirate(80, reservoir_1['B1'],rate=0.7)
	p300.dispense(80, plate['A3'],rate=0.7)
	p300.aspirate(80, reservoir_1['B1'],rate=0.7)
	p300.dispense(80, plate['F6'],rate=0.7)
	p300.aspirate(80, reservoir_1['B1'],rate=0.7)
	p300.dispense(80, plate['C7'],rate=0.7)
	p300.drop_tip()
	#NH4NO3_0_7
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_1['D1'],rate=0.7)
	p300.dispense(80, plate['F2'],rate=0.7)
	p300.aspirate(80, reservoir_1['D1'],rate=0.7)
	p300.dispense(80, plate['A3'],rate=0.7)
	p300.aspirate(80, reservoir_1['D1'],rate=0.7)
	p300.dispense(80, plate['F6'],rate=0.7)
	p300.aspirate(80, reservoir_1['D1'],rate=0.7)
	p300.dispense(80, plate['C7'],rate=0.7)
	p300.drop_tip()
	#MgSO4_0_7
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_2['B1'],rate=0.7)
	p300.dispense(80, plate['F2'],rate=0.7)
	p300.aspirate(80, reservoir_2['B1'],rate=0.7)
	p300.dispense(80, plate['A3'],rate=0.7)
	p300.aspirate(80, reservoir_2['B1'],rate=0.7)
	p300.dispense(80, plate['F6'],rate=0.7)
	p300.aspirate(80, reservoir_2['B1'],rate=0.7)
	p300.dispense(80, plate['C7'],rate=0.7)
	p300.drop_tip()
	#KH2PO4_0_7
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_2['D1'],rate=0.7)
	p300.dispense(80, plate['F2'],rate=0.7)
	p300.aspirate(80, reservoir_2['D1'],rate=0.7)
	p300.dispense(80, plate['A3'],rate=0.7)
	p300.aspirate(80, reservoir_2['D1'],rate=0.7)
	p300.dispense(80, plate['F6'],rate=0.7)
	p300.aspirate(80, reservoir_2['D1'],rate=0.7)
	p300.dispense(80, plate['C7'],rate=0.7)
	p300.drop_tip()
	#Na2HPO4_0_7
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_3['B1'],rate=0.7)
	p300.dispense(80, plate['F2'],rate=0.7)
	p300.aspirate(80, reservoir_3['B1'],rate=0.7)
	p300.dispense(80, plate['A3'],rate=0.7)
	p300.aspirate(80, reservoir_3['B1'],rate=0.7)
	p300.dispense(80, plate['F6'],rate=0.7)
	p300.aspirate(80, reservoir_3['B1'],rate=0.7)
	p300.dispense(80, plate['C7'],rate=0.7)
	p300.drop_tip()
	#Na2EDTA_0_7
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_3['D1'],rate=0.7)
	p300.dispense(80, plate['F2'],rate=0.7)
	p300.aspirate(80, reservoir_3['D1'],rate=0.7)
	p300.dispense(80, plate['A3'],rate=0.7)
	p300.aspirate(80, reservoir_3['D1'],rate=0.7)
	p300.dispense(80, plate['F6'],rate=0.7)
	p300.aspirate(80, reservoir_3['D1'],rate=0.7)
	p300.dispense(80, plate['C7'],rate=0.7)
	p300.drop_tip()
	#CaCl2_0_7
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_4['B1'],rate=0.7)
	p300.dispense(80, plate['F2'],rate=0.7)
	p300.aspirate(80, reservoir_4['B1'],rate=0.7)
	p300.dispense(80, plate['A3'],rate=0.7)
	p300.aspirate(80, reservoir_4['B1'],rate=0.7)
	p300.dispense(80, plate['F6'],rate=0.7)
	p300.aspirate(80, reservoir_4['B1'],rate=0.7)
	p300.dispense(80, plate['C7'],rate=0.7)
	p300.drop_tip()
	#FeSO4_0_7
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_4['D1'],rate=0.7)
	p300.dispense(80, plate['F2'],rate=0.7)
	p300.aspirate(80, reservoir_4['D1'],rate=0.7)
	p300.dispense(80, plate['A3'],rate=0.7)
	p300.aspirate(80, reservoir_4['D1'],rate=0.7)
	p300.dispense(80, plate['F6'],rate=0.7)
	p300.aspirate(80, reservoir_4['D1'],rate=0.7)
	p300.dispense(80, plate['C7'],rate=0.7)
	p300.drop_tip()
	#MnSO4_0_7
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_5['B1'],rate=0.7)
	p300.dispense(80, plate['F2'],rate=0.7)
	p300.aspirate(80, reservoir_5['B1'],rate=0.7)
	p300.dispense(80, plate['A3'],rate=0.7)
	p300.aspirate(80, reservoir_5['B1'],rate=0.7)
	p300.dispense(80, plate['F6'],rate=0.7)
	p300.aspirate(80, reservoir_5['B1'],rate=0.7)
	p300.dispense(80, plate['C7'],rate=0.7)
	p300.drop_tip()
	#Glucose_0_CTRL
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_1['B2'],rate=0.7)
	p300.dispense(80, plate['B5'],rate=0.7)
	p300.aspirate(80, reservoir_1['B2'],rate=0.7)
	p300.dispense(80, plate['B4'],rate=0.7)
	p300.aspirate(80, reservoir_1['B2'],rate=0.7)
	p300.dispense(80, plate['E6'],rate=0.7)
	p300.aspirate(80, reservoir_1['B2'],rate=0.7)
	p300.dispense(80, plate['F3'],rate=0.7)
	p300.drop_tip()
	#NH4NO3_0_CTRL
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_1['D2'],rate=0.7)
	p300.dispense(80, plate['B5'],rate=0.7)
	p300.aspirate(80, reservoir_1['D2'],rate=0.7)
	p300.dispense(80, plate['B4'],rate=0.7)
	p300.aspirate(80, reservoir_1['D2'],rate=0.7)
	p300.dispense(80, plate['E6'],rate=0.7)
	p300.aspirate(80, reservoir_1['D2'],rate=0.7)
	p300.dispense(80, plate['F3'],rate=0.7)
	p300.drop_tip()
	#MgSO4_0_CTRL
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_2['B2'],rate=0.7)
	p300.dispense(80, plate['B5'],rate=0.7)
	p300.aspirate(80, reservoir_2['B2'],rate=0.7)
	p300.dispense(80, plate['B4'],rate=0.7)
	p300.aspirate(80, reservoir_2['B2'],rate=0.7)
	p300.dispense(80, plate['E6'],rate=0.7)
	p300.aspirate(80, reservoir_2['B2'],rate=0.7)
	p300.dispense(80, plate['F3'],rate=0.7)
	p300.drop_tip()
	#KH2PO4_0_CTRL
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_2['D2'],rate=0.7)
	p300.dispense(80, plate['B5'],rate=0.7)
	p300.aspirate(80, reservoir_2['D2'],rate=0.7)
	p300.dispense(80, plate['B4'],rate=0.7)
	p300.aspirate(80, reservoir_2['D2'],rate=0.7)
	p300.dispense(80, plate['E6'],rate=0.7)
	p300.aspirate(80, reservoir_2['D2'],rate=0.7)
	p300.dispense(80, plate['F3'],rate=0.7)
	p300.drop_tip()
	#Na2HPO4_0_CTRL
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_3['B2'],rate=0.7)
	p300.dispense(80, plate['B5'],rate=0.7)
	p300.aspirate(80, reservoir_3['B2'],rate=0.7)
	p300.dispense(80, plate['B4'],rate=0.7)
	p300.aspirate(80, reservoir_3['B2'],rate=0.7)
	p300.dispense(80, plate['E6'],rate=0.7)
	p300.aspirate(80, reservoir_3['B2'],rate=0.7)
	p300.dispense(80, plate['F3'],rate=0.7)
	p300.drop_tip()
	#Na2EDTA_0_CTRL
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_3['D2'],rate=0.7)
	p300.dispense(80, plate['B5'],rate=0.7)
	p300.aspirate(80, reservoir_3['D2'],rate=0.7)
	p300.dispense(80, plate['B4'],rate=0.7)
	p300.aspirate(80, reservoir_3['D2'],rate=0.7)
	p300.dispense(80, plate['E6'],rate=0.7)
	p300.aspirate(80, reservoir_3['D2'],rate=0.7)
	p300.dispense(80, plate['F3'],rate=0.7)
	p300.drop_tip()
	#CaCl2_0_CTRL
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_4['B2'],rate=0.7)
	p300.dispense(80, plate['B5'],rate=0.7)
	p300.aspirate(80, reservoir_4['B2'],rate=0.7)
	p300.dispense(80, plate['B4'],rate=0.7)
	p300.aspirate(80, reservoir_4['B2'],rate=0.7)
	p300.dispense(80, plate['E6'],rate=0.7)
	p300.aspirate(80, reservoir_4['B2'],rate=0.7)
	p300.dispense(80, plate['F3'],rate=0.7)
	p300.drop_tip()
	#FeSO4_0_CTRL
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_4['D2'],rate=0.7)
	p300.dispense(80, plate['B5'],rate=0.7)
	p300.aspirate(80, reservoir_4['D2'],rate=0.7)
	p300.dispense(80, plate['B4'],rate=0.7)
	p300.aspirate(80, reservoir_4['D2'],rate=0.7)
	p300.dispense(80, plate['E6'],rate=0.7)
	p300.aspirate(80, reservoir_4['D2'],rate=0.7)
	p300.dispense(80, plate['F3'],rate=0.7)
	p300.drop_tip()
	#MnSO4_0_CTRL
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_5['B2'],rate=0.7)
	p300.dispense(80, plate['B5'],rate=0.7)
	p300.aspirate(80, reservoir_5['B2'],rate=0.7)
	p300.dispense(80, plate['B4'],rate=0.7)
	p300.aspirate(80, reservoir_5['B2'],rate=0.7)
	p300.dispense(80, plate['E6'],rate=0.7)
	p300.aspirate(80, reservoir_5['B2'],rate=0.7)
	p300.dispense(80, plate['F3'],rate=0.7)
	p300.drop_tip()
	#Glucose_0_REF
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_1['B3'],rate=0.7)
	p300.dispense(80, plate['F5'],rate=0.7)
	p300.aspirate(80, reservoir_1['B3'],rate=0.7)
	p300.dispense(80, plate['B6'],rate=0.7)
	p300.aspirate(80, reservoir_1['B3'],rate=0.7)
	p300.dispense(80, plate['C4'],rate=0.7)
	p300.aspirate(80, reservoir_1['B3'],rate=0.7)
	p300.dispense(80, plate['D4'],rate=0.7)
	p300.drop_tip()
	#NH4NO3_0_REF
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_1['D3'],rate=0.7)
	p300.dispense(80, plate['F5'],rate=0.7)
	p300.aspirate(80, reservoir_1['D3'],rate=0.7)
	p300.dispense(80, plate['B6'],rate=0.7)
	p300.aspirate(80, reservoir_1['D3'],rate=0.7)
	p300.dispense(80, plate['C4'],rate=0.7)
	p300.aspirate(80, reservoir_1['D3'],rate=0.7)
	p300.dispense(80, plate['D4'],rate=0.7)
	p300.drop_tip()
	#MgSO4_0_REF
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_2['B3'],rate=0.7)
	p300.dispense(80, plate['F5'],rate=0.7)
	p300.aspirate(80, reservoir_2['B3'],rate=0.7)
	p300.dispense(80, plate['B6'],rate=0.7)
	p300.aspirate(80, reservoir_2['B3'],rate=0.7)
	p300.dispense(80, plate['C4'],rate=0.7)
	p300.aspirate(80, reservoir_2['B3'],rate=0.7)
	p300.dispense(80, plate['D4'],rate=0.7)
	p300.drop_tip()
	#KH2PO4_0_REF
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_2['D3'],rate=0.7)
	p300.dispense(80, plate['F5'],rate=0.7)
	p300.aspirate(80, reservoir_2['D3'],rate=0.7)
	p300.dispense(80, plate['B6'],rate=0.7)
	p300.aspirate(80, reservoir_2['D3'],rate=0.7)
	p300.dispense(80, plate['C4'],rate=0.7)
	p300.aspirate(80, reservoir_2['D3'],rate=0.7)
	p300.dispense(80, plate['D4'],rate=0.7)
	p300.drop_tip()
	#Na2HPO4_0_REF
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_3['B3'],rate=0.7)
	p300.dispense(80, plate['F5'],rate=0.7)
	p300.aspirate(80, reservoir_3['B3'],rate=0.7)
	p300.dispense(80, plate['B6'],rate=0.7)
	p300.aspirate(80, reservoir_3['B3'],rate=0.7)
	p300.dispense(80, plate['C4'],rate=0.7)
	p300.aspirate(80, reservoir_3['B3'],rate=0.7)
	p300.dispense(80, plate['D4'],rate=0.7)
	p300.drop_tip()
	#Na2EDTA_0_REF
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_3['D3'],rate=0.7)
	p300.dispense(80, plate['F5'],rate=0.7)
	p300.aspirate(80, reservoir_3['D3'],rate=0.7)
	p300.dispense(80, plate['B6'],rate=0.7)
	p300.aspirate(80, reservoir_3['D3'],rate=0.7)
	p300.dispense(80, plate['C4'],rate=0.7)
	p300.aspirate(80, reservoir_3['D3'],rate=0.7)
	p300.dispense(80, plate['D4'],rate=0.7)
	p300.drop_tip()
	#CaCl2_0_REF
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_4['B3'],rate=0.7)
	p300.dispense(80, plate['F5'],rate=0.7)
	p300.aspirate(80, reservoir_4['B3'],rate=0.7)
	p300.dispense(80, plate['B6'],rate=0.7)
	p300.aspirate(80, reservoir_4['B3'],rate=0.7)
	p300.dispense(80, plate['C4'],rate=0.7)
	p300.aspirate(80, reservoir_4['B3'],rate=0.7)
	p300.dispense(80, plate['D4'],rate=0.7)
	p300.drop_tip()
	#FeSO4_0_REF
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_4['D3'],rate=0.7)
	p300.dispense(80, plate['F5'],rate=0.7)
	p300.aspirate(80, reservoir_4['D3'],rate=0.7)
	p300.dispense(80, plate['B6'],rate=0.7)
	p300.aspirate(80, reservoir_4['D3'],rate=0.7)
	p300.dispense(80, plate['C4'],rate=0.7)
	p300.aspirate(80, reservoir_4['D3'],rate=0.7)
	p300.dispense(80, plate['D4'],rate=0.7)
	p300.drop_tip()
	#MnSO4_0_REF
	p300.pick_up_tip()
	p300.aspirate(80, reservoir_5['B3'],rate=0.7)
	p300.dispense(80, plate['F5'],rate=0.7)
	p300.aspirate(80, reservoir_5['B3'],rate=0.7)
	p300.dispense(80, plate['B6'],rate=0.7)
	p300.aspirate(80, reservoir_5['B3'],rate=0.7)
	p300.dispense(80, plate['C4'],rate=0.7)
	p300.aspirate(80, reservoir_5['B3'],rate=0.7)
	p300.dispense(80, plate['D4'],rate=0.7)
	p300.drop_tip()
