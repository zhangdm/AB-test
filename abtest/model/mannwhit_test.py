# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import warnings
from abtest.base.split_batch import split_batch
from scipy.stats import mannwhitneyu
warnings.filterwarnings("ignore")

def U_test(Data,batcha,batchb,alpha,input_power):
    data = pd.DataFrame(Data, dtype='float')
    alpha = float(alpha)
    input_power = float(input_power)

    batcha,batchb = float(batcha),float(batchb)

    dfa,dfb = split_batch(data,batcha,batchb)

    pvalue = mannwhitneyu(dfa['metric'],dfb['metric'],use_continuity=True,alternative='two-sided').pvalue

    avg_a = np.mean(dfa['metric'])
    avg_b = np.mean(dfb['metric'])
    lift = (avg_b - avg_a) / avg_a

    result_df = {'A_metric_avg': avg_a, 'B_metric_avg': avg_b, 'lift': lift, 'lift_interv_down': '--','lift_interv_up': '--', 'pvalue': pvalue, 'power': '--'}
    return result_df