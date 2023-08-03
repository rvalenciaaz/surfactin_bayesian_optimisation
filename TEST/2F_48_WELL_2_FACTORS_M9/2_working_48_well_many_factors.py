#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import string
from functools import reduce
import matplotlib.patches as mpatches

random.seed(1245)

#define the number of factors/dimension and the correspoding iteration index
dim=2
iteration=0

maxwell=800

# Define the number of rows and columns of the microplate
num_rows = 6
num_cols = 8

#Define number of conditions and block
condition_total=9
block_total=4

# Define the well size and radius
well_size = 1.2
well_radius = well_size / 2

#get numbers and letters labels for the wells
columns_labels=[i+1 for i in range(0,num_cols)]
rows_labels=list(reversed(list(string.ascii_uppercase)[0:num_rows]))

#exact axes positions to put the labels
xlabel_pos=[0.6+1.2*i for i in range (0,num_cols)]
ylabel_pos=[0.6+1.2*i for i in range (0,num_rows)]

# Create a new figure
fig = plt.figure(figsize=(12, 8))

# Create a 2D array to represent the microplate
plate = np.zeros((num_rows, num_cols))

# Define the randomized complete block design
conditions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
blocks = [1, 2, 3, 4]
design = []
for block in blocks:
    design += np.random.permutation(conditions).tolist()

data = []
# Loop over each well in the microplate and plot a circle with color
for row in range(num_rows):
    for col in range(num_cols):
        x = col * well_size + well_radius
        y = row * well_size + well_radius
        well_position = rows_labels[row] + str(col + 1)
        if row in range(0, 6) and col in range(1, 7):
            block_row = (row) // 3   #floored quotient
            block_col = (col-1) // 3
            block = block_row*2 + block_col + 1
            block_design = design[(block - 1) * 9:block * 9]
            well_row = (row) % 3
            well_col = (col - 1) % 3
            if block_design[well_row * 3 + well_col]==8:
                condition = str(iteration)+"_REF"
                replicate=  str(iteration)+"_REF_"+str(block)
            elif block_design[well_row * 3 + well_col]==9:
                condition = str(iteration)+"_CTRL"
                replicate=  str(iteration)+"_CTRL_"+str(block)
            else:
                condition = str(iteration)+"_"+str(block_design[well_row * 3 + well_col])
                replicate=  str(iteration)+"_"+str(block_design[well_row * 3 + well_col])+"_"+str(block)
            color = plt.get_cmap('tab10')(block_design[well_row * 3 + well_col] - 1)
        else:
            color = 'lightblue'
            condition = "water"
            replicate=""
        circle = plt.Circle((x, y), well_radius * 0.8, fill=True, edgecolor='black', linewidth=1, facecolor=color)
        plt.gca().add_patch(circle)
        data.append((well_position, condition,replicate,color))
#save color dataframe        
df = pd.DataFrame(data, columns=['well_position', 'sample','replicate',"color"])
df=df.sort_values("well_position")
df.to_csv("color_tables/"+str(iteration)+"_color_table.csv",index=False)

# Set the axis limits and labels
plt.xlim([0, num_cols * well_size])
plt.ylim([0, num_rows * well_size])

plt.xticks(xlabel_pos,columns_labels,fontsize=20)
plt.yticks(ylabel_pos,rows_labels,fontsize=20)

codf=df.groupby("sample").head(1).sort_values("sample")

legi=[mpatches.Patch(color=i["color"], label=i["sample"]) for ind,i in codf.iterrows()]

plt.legend(handles=legi,bbox_to_anchor=(1, 1),fontsize=15)
plt.vlines(x = [4.8], ymin = 0.1, ymax = 7.1,color="black",linewidth=4)
plt.hlines(y = [3.6], xmin = 1.2, xmax = 8.4,color="black",linewidth=4)

plt.savefig("microplate_diagrams/"+str(iteration)+"_microplate_48.jpg",dpi=200,bbox_inches="tight")

#--------------------------------------------------------------------------------------------------

#reading sample table
sam=pd.read_csv("samples/"+str(iteration)+"_samples.csv")
samples=sam.copy()

#defining components minimum concentration, maximum concentration and stock concentration
#reemplazar por dataframe
labels={"Glucose":(0,4,40),"NH4Cl":(0,240,2400),"MgSO4":(0,2,20),"KH2PO4":(0,50,500),
        "Na2HPO4":(0,50,500),"CaCl2":(0,0.2,2)}

maxvol=80

loi=list(labels.keys())
for i in loi:
    samples[i]=maxvol

#samples["extra"]=400
if (maxwell-int(maxwell/10)-dim*maxvol)!=0:
    samples["water"]=(maxwell-int(maxwell/10)-dim*maxvol)
    cux=(maxwell-int(maxwell/10)-dim*maxvol)

#reference values, all volumes set to maxvol
ref_values=pd.DataFrame({"sample":["0_REF","0_CTRL"],"Glucose":[maxvol]*2,"NH4Cl":[maxvol]*2,"MgSO4":[maxvol]*2,"KH2PO4":[maxvol]*2,
        "Na2HPO4":[maxvol]*2,"CaCl2":[maxvol]*2})

#new samples table with volumes
samples=pd.concat([samples,ref_values])

#copying color dataframe
desi=df.copy()
#get well position, sample and replicate
desi=desi[["well_position","sample","replicate"]]

#merge well information with sample volume information
cotable=pd.merge(desi,samples)
#shuffle
cotable=cotable.sample(frac=1).reset_index(drop=True)
#save master table
cotable.to_csv("run_master_table/"+str(iteration)+"_master_table.csv",index=False)


#print(cotable)

#get list of wells ?
well_list=["'"+str(i)+"'," for i in cotable["well_position"]]
well_list=reduce(lambda x,y: x+y, well_list)
well_list="["+well_list[:-1]+"]"

#print(well_list)
#reservoir_well=["A1","A2","A3","B1","B2","B3"]

#what's mici doing?
mici=[]
for ind,i in enumerate(cotable.columns[3:]):
    tmp_list=["{:.2f}".format(j)+"," for j in cotable[i]]
    tmp_list=reduce(lambda x,y: x+y, tmp_list)
    tmp_list="["+tmp_list[:-1]+"]"
    mici.append(tmp_list)

#print(mici)

re1=["A1","A2","A3","A4","A5","A6","B1","B2","B3"]
re2=["C1","C2","C3","C4","C5","C6","D1","D2","D3"]

tem=cotable.sort_values("sample")

re1dict=dict(zip(pd.unique(tem["sample"]),re1))
re2dict=dict(zip(pd.unique(tem["sample"]),re2))

for trind in range(0,dim,2):
    tem[loi[trind]]=tem["sample"].apply(lambda x: re1dict[x])
    if ((dim%2!=1) or (trind!=dim-1)):
        tem[loi[trind+1]]=tem["sample"].apply(lambda x: re2dict[x])

sources={"extra":"A1","water":"A2"}

#setup number of rack

racknumber=int(np.ceil(dim/2))
rackcode={"Glucose":"1","NH4Cl":"1","MgSO4":"2","KH2PO4":"2",
        "Na2HPO4":"3","CaCl2":"3"}


with open("opentrons_scripts/"+str(iteration)+"_opentrons.py","w") as f:
    f.write("from opentrons import protocol_api\nmetadata = {'apiLevel': '2.13'}\ndef run(protocol: protocol_api.ProtocolContext):\n")
    f.write("\tplate = protocol.load_labware('corning_48_wellplate_1.6ml_flat', 8)\n\ttiprack_2 = protocol.load_labware('opentrons_96_tiprack_300ul', 11)\n")
    for rn in range(1, racknumber+1):
        f.write("\treservoir_"+str(rn)+"= protocol.load_labware('opentrons_24_tuberack_eppendorf_2ml_safelock_snapcap',"+str(rn)+")\n")
    f.write("\tbig= protocol.load_labware('corning_6_wellplate_16.8ml_flat',7)\n\tp300 = protocol.load_instrument('p300_single', 'left', tip_racks=[tiprack_2])\n")
    for i in pd.unique(tem["sample"]):
        mini=tem.loc[tem["sample"]==i].copy()
        for compi in mini.columns[3:3+dim]:
            f.write("\t#"+compi+"_"+i+"\n")
            f.write("\tp300.pick_up_tip()\n")
            for res, ving in zip(mini[compi],mini["well_position"]):
                f.write("\tp300.aspirate("+str(maxvol)+", reservoir_"+rackcode[compi]+"['"+res+"'])\n")
                f.write("\tp300.dispense("+str(maxvol)+", plate['"+ving+"'])\n")
                #f.write("\tp10.aspirate(10, reservoir['"+res+"'])\n")
                #f.write("\tp10.dispense(10, plate['"+ving+"'])\n")
            f.write("\tp300.drop_tip()\n")
    print(tem.columns)
    print(3+dim)
    for compi in pd.unique(tem.columns[3+dim:]):
        f.write("\t#"+compi+"\n")
        f.write("\tp300.pick_up_tip()\n")
        if compi!="extra":
            for res, ving in zip(tem[compi],tem["well_position"]):
                f.write("\tp300.aspirate("+str(cux)+", big['"+sources[compi]+"'])\n")
                f.write("\tp300.dispense("+str(cux)+", plate['"+ving+"'])\n")
        else:
            for res, ving in zip(tem[compi],tem["well_position"]):
                f.write("\tp300.aspirate("+str(res)+", big['"+sources[compi]+"'])\n")
                f.write("\tp300.dispense("+str(res)+", plate['"+ving+"'])\n")
                #f.write("\tp300.aspirate(200, big['"+sources[compi]+"'])\n")
                #f.write("\tp300.dispense(200, plate['"+ving+"'])\n")
        f.write("\tp300.drop_tip()\n")
with open("ms_run_tables/"+str(iteration)+"_ms_table.csv","w") as g:
    g.write("Bracket Type=4,,,,,,,,,,,,,,,,,,,,\n")
    g.write("Sample Type,File Name,Sample ID,Path,Instrument Method,Process Method,Calibration File,Position,Inj Vol,Level,Sample Wt,Sample Vol,ISTD Amt,Dil Factor,L1 Study,L2 Client,L3 Laboratory,L4 Company,L5 Phone,Comment,Sample Name\n")
    g.write("Blank,"+str(iteration)+"_Blank_1,"+str(iteration)+"_Blank_1,C:\Xcalibur\Data\Richie\\0_experiment,C:\Xcalibur\methods\Richie\\200_Richie_flow_injection_Surfactin_pumpmodule_15aux_ACN_b,C:\Xcalibur\methods\Richie\QQQ_FlowInjection_Surfactin,,RA6,1,,0,0,0,1,,,,,,,\n")
    g.write("Blank,"+str(iteration)+"_Blank_2,"+str(iteration)+"_Blank_2,C:\Xcalibur\Data\Richie\\0_experiment,C:\Xcalibur\methods\Richie\\200_Richie_flow_injection_Surfactin_pumpmodule_15aux_ACN_b,C:\Xcalibur\methods\Richie\QQQ_FlowInjection_Surfactin,,RA6,1,,0,0,0,1,,,,,,,\n")
    g.write("Blank,"+str(iteration)+"_Blank_3,"+str(iteration)+"_Blank_3,C:\Xcalibur\Data\Richie\\0_experiment,C:\Xcalibur\methods\Richie\\200_Richie_flow_injection_Surfactin_pumpmodule_15aux_ACN_b,C:\Xcalibur\methods\Richie\QQQ_FlowInjection_Surfactin,,RA6,1,,0,0,0,1,,,,,,,\n")
    for ind,i in cotable.iterrows():
        if ind%6==0:
            g.write("Unknown,QC_"+str(int(ind/6)+1)+",QC_"+str(int(ind/6)+1)+",C:\Xcalibur\Data\Richie\\0_experiment,C:\Xcalibur\methods\Richie\\200_Richie_flow_injection_Surfactin_pumpmodule_15aux_ACN_b,C:\Xcalibur\methods\Richie\QQQ_FlowInjection_Surfactin,,RA7,1,,0,0,0,1,,,,,,,\n")
            g.write("Unknown,"+i["replicate"]+","+i["replicate"]+",C:\Xcalibur\Data\Richie\\0_experiment,C:\Xcalibur\methods\Richie\\200_Richie_flow_injection_Surfactin_pumpmodule_15aux_ACN_b,C:\Xcalibur\methods\Richie\QQQ_FlowInjection_Surfactin,,B"+i["well_position"]+",1,,0,0,0,1,,,,,,,\n")
        else:
            g.write("Unknown,"+i["replicate"]+","+i["replicate"]+",C:\Xcalibur\Data\Richie\\0_experiment,C:\Xcalibur\methods\Richie\\200_Richie_flow_injection_Surfactin_pumpmodule_15aux_ACN_b,C:\Xcalibur\methods\Richie\QQQ_FlowInjection_Surfactin,,B"+i["well_position"]+",1,,0,0,0,1,,,,,,,\n")
    g.write("Blank,"+str(iteration)+"_Blank_4,"+str(iteration)+"_Blank_4,C:\Xcalibur\Data\Richie\\0_experiment,C:\Xcalibur\methods\Richie\\200_Richie_flow_injection_Surfactin_pumpmodule_15aux_ACN_b,C:\Xcalibur\methods\Richie\QQQ_FlowInjection_Surfactin,,RA6,1,,0,0,0,1,,,,,,,\n")
    g.write("Blank,"+str(iteration)+"_Blank_5,"+str(iteration)+"_Blank_5,C:\Xcalibur\Data\Richie\\0_experiment,C:\Xcalibur\methods\Richie\\200_Richie_flow_injection_Surfactin_pumpmodule_15aux_ACN_b,C:\Xcalibur\methods\Richie\QQQ_FlowInjection_Surfactin,,RA6,1,,0,0,0,1,,,,,,,\n")
    g.write("Blank,"+str(iteration)+"_Blank_6,"+str(iteration)+"_Blank_6,C:\Xcalibur\Data\Richie\\0_experiment,C:\Xcalibur\methods\Richie\\200_Richie_flow_injection_Surfactin_pumpmodule_15aux_ACN_b,C:\Xcalibur\methods\Richie\QQQ_FlowInjection_Surfactin,,RA6,1,,0,0,0,1,,,,,,,\n")

