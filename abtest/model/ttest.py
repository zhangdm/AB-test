# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from abtest.base.base_t_test import ttest
import warnings
warnings.filterwarnings('ignore')

def t_test(data,batcha,batchb,alpha,input_power,ttest_plus_method=False):
    """

    :param data:
    :param batcha:
    :param batchb:
    :param alpha:
    :param input_power:
    :param ttest_plus_method:
    :return:
    """
    ## 划分数据集
    dfa = data[data['batch'] == float(batcha)]
    dfb = data[data['batch'] == float(batchb)]

    result_dict = ttest(dfa,dfb,float(alpha),input_power,ttest_plus_method)
    return (result_dict)
