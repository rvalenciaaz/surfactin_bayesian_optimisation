#!/usr/bin/env python
# coding: utf-8


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import string
from functools import reduce
import matplotlib.patches as mpatches

dim=7
iteration=0
voly=5000
maxwell=800
maxvol=80

stock=pd.read_csv("stock_table_M9.csv")
dic1=dict(zip(stock["compound"],stock["max_concentration_mM"]))

cooper=pd.read_csv("M9_preparation.csv")
dic2=dict(zip(cooper["compound"],cooper["M9_concentration_mM"]))

sam=pd.read_csv("samples/"+str(iteration)+"_samples.csv")
samples=sam.copy()

compi=["Glucose","NH4Cl","MgSO4","KH2PO4","Na2HPO4","CaCl2","NaCl"]

#adding standard concentration for fixed compounds
nen=list(set(compi)-set(samples.columns[1:]))
dictio1={i:dic1[i] for i in nen}
dictio2={i:dic2[i] for i in nen}

for k in nen:
    samples[k]=dictio2[k]/dictio1[k]

#add CTRL and REF
#['sample', 'Glucose', 'NH4NO3', 'KH2PO4', 'Na2HPO4', 'FeSO4', 'MnSO4','MgSO4', 'Na2EDTA', 'CaCl2']

cor=[(dic2[k]/dic1[k]) for k in list(samples.columns) if (k!="sample")]

standard1=[str(iteration)+"_CTRL"]+cor
standard2=[str(iteration)+"_REF"]+cor

stdf=pd.DataFrame(columns=samples.columns)

stdf.loc[0]=standard1
stdf.loc[1]=standard2

samples=pd.concat([samples,stdf]).reset_index(drop=True)

#print(samples)
#stock data
labels={"Glucose":(0,4,40),"NH4Cl":(0,240,2400),"MgSO4":(0,2,20),"KH2PO4":(0,50,500),
        "Na2HPO4":(0,50,500),"CaCl2":(0,0.2,2),"NaCl":(0,50,500)}

for j in samples.columns[1:]:
    samples["Vol_"+j]=round(((samples[j]*labels[j][1])*maxwell/maxvol)*voly/labels[j][2],1)
    samples["Water_"+j]=round(voly-samples["Vol_"+j],1)


newcol=["sample"]+[z for z in list(samples.columns) if (("Vol" in z) or ("Water" in z))]

newdf=samples[newcol].copy()

newdf.to_csv("tube_stock/"+str(iteration)+"_tube_stock.csv", index=False)
newdf.to_excel("tube_stock/"+str(iteration)+"_tube_stock.xlsx", index=False)