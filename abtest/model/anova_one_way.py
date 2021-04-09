# -*- coding: utf-8 -*-

## 假设数据服从二项分布,依据超几何分布求pvalue

import pandas as pd
import numpy as np
import warnings
from abtest.base.split_batch import split_batch
from scipy.stats import f_oneway
warnings.filterwarnings("ignore")

def anova_test(Data,batcha,batchb,alpha,input_power):
    data = pd.DataFrame(Data, dtype='float')
    alpha = float(alpha)
    input_power = float(input_power)

    batcha,batchb = float(batcha),float(batchb)

    dfa,dfb = split_batch(data,batcha,batchb)

    N_a_0 = np.sum(dfa['metric'].isin([0]))
    N_b_0 = np.sum(dfb['metric'].isin([0]))

    pvalue = f_oneway(dfa['metric'],dfb['metric'])[1]

    avg_a = (dfa.shape[0] - N_a_0) / float(dfa.shape[0])
    avg_b = (dfb.shape[0] - N_b_0) / float(dfb.shape[0])
    lift = (avg_b - avg_a) / avg_a

    result_df = {'A_metric_avg': avg_a, 'B_metric_avg': avg_b, 'lift': lift, 'lift_interv_down': '--','lift_interv_up': '--', 'pvalue': pvalue, 'power': '--'}
    return result_df