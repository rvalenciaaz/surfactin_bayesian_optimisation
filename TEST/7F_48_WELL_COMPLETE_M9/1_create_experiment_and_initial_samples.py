#!/usr/bin/env python
# coding: utf-8

import os
import torch
import random
import numpy as np
import pandas as pd
from botorch.models import SingleTaskGP, HeteroskedasticSingleTaskGP
from botorch.fit import fit_gpytorch_mll
from botorch.acquisition import UpperConfidenceBound,qUpperConfidenceBound
from botorch.optim import optimize_acqf
from botorch.utils.sampling import draw_sobol_samples
from gpytorch.mlls import ExactMarginalLogLikelihood
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from sklearn.preprocessing import MinMaxScaler

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
dtype = torch.float64

seed = 1245

random.seed(seed)
torch.manual_seed(seed)
torch.backends.cudnn.deterministic = True
if torch.cuda.is_available(): torch.cuda.manual_seed_all(seed)
np.random.seed(seed)

directories = ["samples", "samples_runned", "raw_data", "opentrons_scripts",
               "microplate_diagrams", "run_master_table", "ms_run_tables", "color_tables","tube_stock"]

for directory in directories:
    if not os.path.exists(directory):
        os.mkdir(directory)
    else:
        print(f"The directory '{directory}' already exists.")

#can be changed
dim = 7
iteration = 0

bounds = torch.stack([torch.zeros(dim,dtype=dtype, device=device), torch.ones(dim,dtype=dtype, device=device)])

#can be changed
init_samples=7

sampler = draw_sobol_samples(bounds=bounds, n=init_samples, q=1).reshape(init_samples,dim)

labels=[str(iteration)+"_"+str(i+1) for i in range(init_samples)]

#can be changed
col_labels=["Glucose","NH4Cl","MgSO4","KH2PO4","Na2HPO4","CaCl2","NaCl"]

init_table = pd.DataFrame({"sample":labels})

init_table[col_labels]=sampler.cpu().numpy()

init_table.to_csv("samples/"+str(iteration)+"_samples.csv",index=False)
