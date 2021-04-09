# -*- coding: utf-8 -*-

'''
处理两种异常情况：
1）存在缺失值
2）至少一组数据全为零
'''

import pandas as pd
import numpy as np
from abtest.base.split_batch import split_batch


def data_checking(data,batcha,batchb):
    dfa,dfb = split_batch(data,batcha,batchb)

    if np.sum(data.isnull().any()) == 0:  ## 没有缺失值
        if np.sum(dfa['metric']) > 0 and np.sum(dfb['metric']) > 0:
            return data
        else:  # 其中至少一组全为零
            return {'resultMsg': "Some groups are zeros", 'resultCode': 402, 'success': true}
    else:
        return {'resultMsg': "Hvae some null values", 'resultCode': 402, 'success': true}