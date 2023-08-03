from opentrons import protocol_api
metadata = {'apiLevel': '2.13'}
def run(protocol: protocol_api.ProtocolContext):
	plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 8)
	tiprack_1 = protocol.load_labware('opentrons_96_tiprack_10ul', 10)
	tiprack_2 = protocol.load_labware('opentrons_96_tiprack_300ul', 11)
	reservoir= protocol.load_labware('corning_6_wellplate_16.8ml_flat',7)
	p10 = protocol.load_instrument('p10_single', 'right', tip_racks=[tiprack_1])
	p300 = protocol.load_instrument('p300_single', 'left', tip_racks=[tiprack_2])
	plate_list=['B9','G7','E10','E6','B4','G2','D9','D5','G5','G9','B6','E3','E5','F5','F6','C8','C2','D8','B3','E9','C3','F2','C9','B2','B5','F8','E7','D7','E8','D6','E4','B7','F4','G10','G4','F7','D2','C10','G6','F9','F3','D3','B8','E2','G3','C4','D4','D10','C6','G8','F10','C7','C5','B10']
	#Glucose
	vol_A1=[20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00]
	#NH4Cl
	vol_A2=[20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00,20.00]
	#extra
	vol_A3=[100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00,100.00]
	#water
	vol_B1=[160.00,160.00,160.00,160.00,160.00,160.00,160.00,60.00,60.00,60.00,60.00,60.00,160.00,160.00,160.00,60.00,60.00,160.00,160.00,160.00,160.00,160.00,60.00,60.00,160.00,160.00,60.00,160.00,60.00,160.00,160.00,160.00,160.00,160.00,160.00,160.00,160.00,160.00,160.00,160.00,60.00,160.00,160.00,160.00,160.00,160.00,160.00,160.00,160.00,160.00,160.00,160.00,160.00,160.00]
	p10.pick_up_tip()
	for voli,cor in zip(vol_A1,plate_list):
		if voli>=40:
			p300.aspirate(voli, reservoir['A1'])
			p300.dispense(voli, plate[cor])
		else:
			for rep in range(0,int(voli/10)+1):
				if rep==int(voli/10):
					p10.aspirate(voli%10, reservoir['A1'])
					p10.dispense(voli%10, plate[cor])
				else:
					p10.aspirate(10, reservoir['A1'])
					p10.dispense(10, plate[cor])
	p10.drop_tip()
	p10.pick_up_tip()
	for voli,cor in zip(vol_A2,plate_list):
		if voli>=40:
			p300.aspirate(voli, reservoir['A2'])
			p300.dispense(voli, plate[cor])
		else:
			for rep in range(0,int(voli/10)+1):
				if rep==int(voli/10):
					p10.aspirate(voli%10, reservoir['A2'])
					p10.dispense(voli%10, plate[cor])
				else:
					p10.aspirate(10, reservoir['A2'])
					p10.dispense(10, plate[cor])
	p10.drop_tip()
	p10.pick_up_tip()
	p300.pick_up_tip()
	for voli,cor in zip(vol_A3,plate_list):
		if voli>=40:
			p300.aspirate(voli, reservoir['A3'])
			p300.dispense(voli, plate[cor])
		else:
			for rep in range(0,int(voli/10)+1):
				if rep==int(voli/10):
					p10.aspirate(voli%10, reservoir['A3'])
					p10.dispense(voli%10, plate[cor])
				else:
					p10.aspirate(10, reservoir['A3'])
					p10.dispense(10, plate[cor])
	p10.drop_tip()
	p300.drop_tip()
	p10.pick_up_tip()
	p300.pick_up_tip()
	for voli,cor in zip(vol_B1,plate_list):
		if voli>=40:
			p300.aspirate(voli, reservoir['B1'])
			p300.dispense(voli, plate[cor])
		else:
			for rep in range(0,int(voli/10)+1):
				if rep==int(voli/10):
					p10.aspirate(voli%10, reservoir['B1'])
					p10.dispense(voli%10, plate[cor])
				else:
					p10.aspirate(10, reservoir['B1'])
					p10.dispense(10, plate[cor])
	p10.drop_tip()
	p300.drop_tip()
