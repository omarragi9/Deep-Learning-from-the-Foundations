
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: dev_nb/_02_fully_connected.ipynb
from pathlib import Path
import os
import torchvision.datasets as datasets
from IPython.core.debugger import set_trace
import pickle, gzip, math, torch, matplotlib as mpl
import matplotlib.pyplot as plt
from torch import tensor
import torch

def get_data():
    root = 'C:\\Users\\omar_\\Part 2 Deep Learning from the Foundations\\data'
    if not os.path.exists(root):
        os.mkdir(root)
    train_set = datasets.MNIST(root = root , train = True , download = False)
    test_set = datasets.MNIST(root = root , train = False , download = False)
    x_train, x_valid = train_set.train_data.split([50000, 10000])
    y_train, y_valid = train_set.train_labels.split([50000, 10000])
    return (x_train.view(50000, -1) / 256.0), y_train.float(), (x_valid.view(10000, -1))/ 256.0, y_valid.float()

def normalize(x , m , s): return (x - m) / s

def test_near_zero(a,tol=1e-3): assert a.abs()<tol, f"Near zero: {a}"

def mse(x , y):
    return (x.squeeze(-1) - y).pow(2).mean()

from torch import nn