#!/usr/bin/env python
# coding: utf-8


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import string
from functools import reduce
import matplotlib.patches as mpatches

dim=6
iteration=0
voly=5000
maxwell=800
maxvol=80

stock=pd.read_csv("stock_table.csv")
dic1=dict(zip(stock["compound"],stock["max_concentration_mM"]))

cooper=pd.read_csv("cooper_preparation.csv")
dic2=dict(zip(cooper["compound"],cooper["cooper_concentration_mM"]))

sam=pd.read_csv("samples/"+str(iteration)+"_samples.csv")
samples=sam.copy()

compi=["Glucose","NH4NO3","MgSO4","KH2PO4",
        "Na2HPO4","Na2EDTA","CaCl2","FeSO4","MnSO4"]

#adding standard concentration for fixed compounds
nen=list(set(compi)-set(samples.columns[1:]))
dictio1={i:dic1[i] for i in nen}
dictio2={i:dic2[i] for i in nen}

for k in nen:
    samples[k]=dictio2[k]/dictio1[k]

#stock data
labels={"Glucose":(0,4,40),"NH4NO3":(0,240,2400),"MgSO4":(0,2,20),"KH2PO4":(0,50,500),
        "Na2HPO4":(0,50,500),"Na2EDTA":(0,0.2,2),"CaCl2":(0,0.2,2),"FeSO4":(0,0.2,2),"MnSO4":(0,0.2,2)}

for j in samples.columns[1:]:
    samples["Vol_"+j]=((samples[j]*labels[j][1])*maxwell/maxvol)*voly/labels[j][2]
    samples["Water_"+j]=voly-samples["Vol_"+j]


newcol=["sample"]+[z for z in list(samples.columns) if (("Vol" in z) or ("Water" in z))]

newdf=samples[newcol].copy()

newdf.to_csv("tube_stock/"+str(iteration)+"_tube_stock.csv", index=False)