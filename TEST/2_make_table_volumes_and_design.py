#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import string
from functools import reduce
import matplotlib.patches as mpatches

dim=2
iteration=0

# Define the number of rows and columns of the microplate
num_rows = 8
num_cols = 12

# Define the well size and radius
well_size = 1.2
well_radius = well_size / 2

columns_labels=[i+1 for i in range(0,12)]
rows_labels=list(reversed(list(string.ascii_uppercase)[0:8]))

xlabel_pos=[0.6+1.2*i for i in range (0,12)]
ylabel_pos=[0.6+1.2*i for i in range (0,8)]

# Create a new figure
fig = plt.figure(figsize=(12, 8))

# Create a 2D array to represent the microplate
plate = np.zeros((num_rows, num_cols))

# Define the randomized complete block design
conditions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
blocks = [1, 2, 3, 4, 5, 6]
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
        if row in range(1, 7) and col in range(1, 10):
            block_row = (row - 1) // 3   #floored quotient
            block_col = (col - 1) // 3
            block = block_row * 3 + block_col + 1
            block_design = design[(block - 1) * 9:block * 9]
            well_row = (row - 1) % 3
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
            color = plt.cm.get_cmap('tab10')(block_design[well_row * 3 + well_col] - 1)
        else:
            color = 'lightblue'
            condition = "water"
            replicate=""
        circle = plt.Circle((x, y), well_radius * 0.8, fill=True, edgecolor='black', linewidth=1, facecolor=color)
        plt.gca().add_patch(circle)
        data.append((well_position, condition,replicate,color))
        
df = pd.DataFrame(data, columns=['well_position', 'sample','replicate',"color"])
df=df.sort_values("well_position")

# Set the axis limits and labels
plt.xlim([0, num_cols * well_size])
plt.ylim([0, num_rows * well_size])

plt.xticks(xlabel_pos,columns_labels,fontsize=20)
plt.yticks(ylabel_pos,rows_labels,fontsize=20)

codf=df.groupby("sample").head(1).sort_values("sample")

legi=[mpatches.Patch(color=i["color"], label=i["sample"]) for ind,i in codf.iterrows()]

plt.legend(handles=legi,bbox_to_anchor=(1, 1),fontsize=15)
plt.vlines(x = [4.8,8.4], ymin = 1.2, ymax = 8.4,color="black",linewidth=4)
plt.hlines(y = [4.8], xmin = 1.2, xmax = 11.9,color="black",linewidth=4)

plt.savefig("microplate_diagrams/"+str(iteration)+"_microplate.jpg",dpi=200,bbox_inches="tight")

sam=pd.read_csv("samples/"+str(iteration)+"_samples.csv")
samples=sam.copy()

#stock data
labels={"Glucose":(0,4,40),"NH4Cl":(0,240,2400)}

for i in list(labels.keys()):
    samples[i]=20
    #samples[i]=samples[i]*200/labels[i][2]

samples["extra"]=100
samples["water"]=160
#for i in list(labels.keys()):
#    samples["water"]=samples["water"]-samples[i]
    

#reference medium values
ref_values=pd.DataFrame({"sample":["0_REF","0_CTRL"],"Glucose":[20,20],"NH4Cl":[20,20],"extra":[100,100],"water":[60,60]})
samples=pd.concat([samples,ref_values])

desi=df.copy()
desi=desi[["well_position","sample","replicate"]]

cotable=pd.merge(desi,samples)
cotable=cotable.sample(frac=1).reset_index(drop=True)

cotable.to_csv("run_master_table/"+str(iteration)+"_master_table.csv",index=False)

well_list=["'"+str(i)+"'," for i in cotable["well_position"]]
well_list=reduce(lambda x,y: x+y, well_list)
well_list="["+well_list[:-1]+"]"

reservoir_well=["A1","A2","A3","B1","B2","B3"]

mici=[]
for ind,i in enumerate(cotable.columns[3:]):
    tmp_list=["{:.2f}".format(j)+"," for j in cotable[i]]
    tmp_list=reduce(lambda x,y: x+y, tmp_list)
    tmp_list="["+tmp_list[:-1]+"]"
    mici.append(tmp_list)

#make opentrons script

with open("opentrons_scripts/"+str(iteration)+"_opentrons.py","w") as f:
    f.write("from opentrons import protocol_api\nmetadata = {'apiLevel': '2.13'}\ndef run(protocol: protocol_api.ProtocolContext):\n")
    f.write("\tplate = protocol.load_labware('corning_96_wellplate_360ul_flat', 8)\n\ttiprack_1 = protocol.load_labware('opentrons_96_tiprack_10ul', 10)\n\ttiprack_2 = protocol.load_labware('opentrons_96_tiprack_300ul', 11)\n\treservoir= protocol.load_labware('corning_6_wellplate_16.8ml_flat',7)\n\tp10 = protocol.load_instrument('p10_single', 'right', tip_racks=[tiprack_1])\n\tp300 = protocol.load_instrument('p300_single', 'left', tip_racks=[tiprack_2])\n")
    f.write("\tplate_list="+well_list+"\n")
    for ind,i in enumerate(cotable.columns[3:]):
        f.write("\t#"+i+"\n")
        f.write("\tvol_"+reservoir_well[ind]+"="+mici[ind]+"\n")
    for ind,i in enumerate(cotable.columns[3:]):
        f.write("\tp10.pick_up_tip()\n")
        if (cotable[i]>=50).sum() >=1:
            f.write("\tp300.pick_up_tip()\n")
        f.write("\tfor voli,cor in zip(vol_"+reservoir_well[ind]+",plate_list):\n")
        f.write("\t\tif voli>=40:\n")
        #f.write("\t\t\tp300.transfer(voli, reservoir['"+reservoir_well[ind]+"'],plate[cor],newtip='never',carryover=True)\n")
        f.write("\t\t\tp300.aspirate(voli, reservoir['"+reservoir_well[ind]+"'])\n")
        f.write("\t\t\tp300.dispense(voli, plate[cor])\n")
        f.write("\t\telse:\n")
        #f.write("\t\t\tp10.transfer(voli, reservoir['"+reservoir_well[ind]+"'],plate[cor],newtip='never',carryover=True)\n")
        #f.write("\t\t\tif voli>=10:\n")
        f.write("\t\t\tfor rep in range(0,int(voli/10)+1):\n")
        f.write("\t\t\t\tif rep==int(voli/10):\n")
        f.write("\t\t\t\t\tp10.aspirate(voli%10, reservoir['"+reservoir_well[ind]+"'])\n")
        f.write("\t\t\t\t\tp10.dispense(voli%10, plate[cor])\n")
        f.write("\t\t\t\telse:\n")
        f.write("\t\t\t\t\tp10.aspirate(10, reservoir['"+reservoir_well[ind]+"'])\n")
        f.write("\t\t\t\t\tp10.dispense(10, plate[cor])\n")
        f.write("\tp10.drop_tip()\n")
        if (cotable[i]>=50).sum() >=1:
            f.write("\tp300.drop_tip()\n")

#make ms table

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


