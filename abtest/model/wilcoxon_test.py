# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import warnings
from abtest.base.split_batch import split_batch
from scipy.stats import ranksums
warnings.filterwarnings("ignore")

def rank_sum_test(Data,batcha,batchb,alpha,input_power):
    data = pd.DataFrame(Data, dtype='float')
    alpha = float(alpha)
    input_power = float(input_power)

    batcha = float(batcha)
    batchb = float(batchb)

    dfa,dfb = split_batch(data,batcha,batchb)

    pvalue = ranksums(dfa['metric'],dfb['metric']).pvalue

    avg_a = np.mean(dfa['metric'])
    avg_b = np.mean(dfb['metric'])
    lift = (avg_b - avg_a) / avg_a

    result_df = {'A_metric_avg': avg_a, 'B_metric_avg': avg_b, 'lift': lift, 'lift_interv_down': '--','lift_interv_up': '--', 'pvalue': pvalue, 'power': '--'}
    return result_df