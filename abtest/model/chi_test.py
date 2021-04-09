# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import warnings
from abtest.base.split_batch import split_batch
from scipy.stats import chi2_contingency
warnings.filterwarnings("ignore")

def chi_test(Data,batcha,batchb,alpha,input_power):
    data = pd.DataFrame(Data,dtype='float')
    alpha = float(alpha)
    input_power = float(input_power)

    batcha, batchb = float(batcha), float(batchb)

    dfa, dfb = split_batch(data, batcha, batchb)

    N_a_0 = np.sum(dfa['metric'].isin([0]))
    N_b_0 = np.sum(dfb['metric'].isin([0]))

    d = np.array([[dfa.shape[0] - N_a_0, N_a_0], [dfb.shape[0] - N_b_0, N_b_0]])
    pvalue = chi2_contingency(d)[1]

    avg_a = (dfa.shape[0] - N_a_0) / (1.000*dfa.shape[0])
    avg_b = (dfb.shape[0] - N_b_0) / (1.000*dfb.shape[0])
    lift = (avg_b - avg_a) / avg_a

    result_df = {'A_metric_avg': avg_a, 'B_metric_avg': avg_b, 'lift': lift, 'lift_interv_down': '--','lift_interv_up': '--', 'pvalue': pvalue, 'power': '--'}
    return result_df
