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

os.mkdir("samples")
os.mkdir("samples_runned")
os.mkdir("raw_data")
os.mkdir("opentrons_scripts")
os.mkdir("microplate_diagrams")
os.mkdir("run_master_table")
os.mkdir("ms_run_tables")

dim = 2
iteration = 0

bounds = torch.stack([torch.zeros(dim,dtype=dtype, device=device), torch.ones(dim,dtype=dtype, device=device)])

init_samples=21

sampler = draw_sobol_samples(bounds=bounds, n=init_samples, q=1).reshape(init_samples,dim)

labels=[str(iteration)+"_"+str(i+1) for i in range(init_samples)]
col_labels=["Glucose","NH4Cl"]

init_table = pd.DataFrame({"sample":labels})

init_table[col_labels]=sampler.cpu().numpy()

init_table.to_csv("samples/"+str(iteration)+"_samples.csv",index=False)