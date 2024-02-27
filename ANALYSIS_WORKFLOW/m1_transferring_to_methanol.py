from opentrons import protocol_api
metadata = {'apiLevel': '2.13'}
def run(protocol: protocol_api.ProtocolContext):
	plate = protocol.load_labware('corning_48_wellplate_1.6ml_flat', 8)
	tiprack_2 = protocol.load_labware('opentrons_96_tiprack_1000ul', 7)
	reservoir = protocol.load_labware('nest_96_wellplate_2ml_deep',5)
	p1000 = protocol.load_instrument('p1000_single', 'right', tip_racks=[tiprack_2])
	
	extr=["A"+str(i) for i in range(2,8)]+["B"+str(i) for i in range(2,8)]+["C"+str(i) for i in range(2,8)]+["D"+str(i) for i in range(2,8)]+["E"+str(i) for i in range(2,8)]+["F"+str(i) for i in range(2,8)]
	revi=["A"+str(i) for i in range(1,13)]+["B"+str(i) for i in range(1,13)]+["C"+str(i) for i in range(1,13)]
	
	dictio=dict(zip(extr,revi))
	for k in list(dictio.keys()):
		p1000.pick_up_tip()
		p1000.aspirate(500, plate[k],rate=0.7)
		p1000.dispense(500, reservoir[dictio[k]],rate=0.7)
		p1000.blow_out()
		p1000.drop_tip()
