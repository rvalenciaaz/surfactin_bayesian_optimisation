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

sam=pd.read_csv("samples/"+str(iteration)+"_samples.csv")
samples=sam.copy()

#stock data
labels={"Glucose":(0,4,40),"NH4NO3":(0,240,2400),"MgSO4":(0,2,20),"KH2PO4":(0,50,500),
        "Na2HPO4":(0,50,500),"Na2EDTA":(0,0.2,2),"CaCl2":(0,0.2,2),"FeSO4":(0,0.2,2),"MnSO4":(0,0.2,2)}

for j in samples.columns[1:dim+1]:
    samples["Vol_"+j]=((samples[j]*labels[j][1])*800/80)*2000/labels[j][2]
    samples["Water_"+j]=2000-samples["Vol_"+j]
    print(samples)
