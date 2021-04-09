# -*- coding: utf-8 -*-
from scipy import stats

def power(avg_a,avg_b,stdab,alpha,Dfree):
    power = 1 - stats.norm.cdf(stats.t.ppf(1 - alpha / 2, Dfree) - (avg_b - avg_a) / stdab) + stats.norm.cdf(-stats.t.ppf(1 - alpha / 2, Dfree) - (avg_b - avg_a) / stdab)
    return power