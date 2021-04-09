# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from decimal import *
getcontext().prec = 28


def get_dataa(maxa):
    maxa = int(maxa)
    dataa = pd.DataFrame({
            'uid':np.arange(2000),
            'metric':np.random.randint(0,maxa,2000),
            'batch':np.random.randint(1,2,2000)
    },columns=['uid','metric','batch'])


    return dataa


def get_datab(maxb):
    maxb = int(maxb)
    datab = pd.DataFrame({
        'uid': np.arange(1000),
        'metric': np.random.randint(0, maxb, 1000),
        'batch': np.random.randint(2, 3,1000)
    }, columns=['uid', 'metric', 'batch'])

    return datab

def data(maxa,maxb):
    dataa = get_dataa(maxa)
    datab = get_datab(maxb)
    data = pd.concat([dataa,datab])
    return data