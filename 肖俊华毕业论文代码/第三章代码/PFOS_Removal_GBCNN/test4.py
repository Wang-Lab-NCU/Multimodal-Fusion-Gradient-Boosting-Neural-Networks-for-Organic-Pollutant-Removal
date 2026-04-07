import torch
import torch.nn as nn
import torch.optim as optim
from utils import mix_seed
from data3 import get_data, get_dataloader
import torch.utils.data as Data
import copy
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np
from model import get_1dcnn_model
import pandas as pd
import matplotlib.pyplot as plt
path = 'pfas_nalv - 副本.xlsx'
columns_list = ['Membrane type', 'MWCO(Da)', 'Pore size(nm)', 'water flux(LMH)', 'Temperature (˚C)', 'PFOS con (ppb)',
                'pH',
                'Pressure (MPa)', 'Divalent cations (mmol/L)',
                'Monovalent cations (mmol/L)', 'Trivalent cations (mmol/L)',
                'PFOS rejection (%)']
df_all = pd.read_excel(path)
df_all = df_all.drop(['Data'], axis=1)