# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")



def get_dataa(maxa):
    maxa = int(maxa)
    dataa = pd.DataFrame({
            'uid':np.arange(100),
            'metric':np.random.randint(0,maxa,100),
            'batch':np.random.randint(1,2,100)
    },columns=['uid','metric','batch'])

    return dataa

def get_datab(maxb):
    maxb = int(maxb)
    datab = pd.DataFrame({
        'uid': np.arange(100),
        'metric': np.random.randint(0, maxb, 100),
        'batch': np.random.randint(2, 3, 100)
    }, columns=['uid', 'metric','batch'])

    return datab
def dataab(maxa,maxb):
    dataa = get_dataa(maxa)
    datab = get_datab(maxb)
    data = pd.concat([dataa,datab])
    return data




