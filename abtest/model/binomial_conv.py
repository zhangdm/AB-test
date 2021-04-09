# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from scipy import stats

def bin_conv(Xa,Xb,Na,Nb):
    Xa,Xb,Na,Nb = float(Xa),float(Xb),float(Na),float(Nb)
    avg_a = Xa / Na
    avg_b = Xb / Nb

    lift = (avg_b - avg_a) / avg_a

    ppool = (Xa+Xb) / (Na+Nb)
    se = np.sqrt(ppool*(1-ppool) * (2/5000.00))

    d = avg_b - avg_a

    m = 1.96*se
    down = (d - m) / avg_a
    up = (d + m) / avg_a
    stat = abs(d) / se
    p = stats.norm.cdf(-stat) * 2

    Power = 1 - stats.norm.cdf(stats.norm.ppf(1 - 0.05 / 2) - (avg_b - avg_a) / se) + stats.norm.cdf(-stats.norm.ppf(1 - 0.05/ 2) - (avg_b - avg_a) / se)

    result = {}
    result['avg_a'] = avg_a
    result['avg_b'] = avg_b
    result['lift'] = lift
    result['lift_down'] = down
    result['lift_up'] = up
    result['pvalue'] = p
    result['power'] = Power

    return result