# -*- coding: utf-8 -*-


from abtest.model.ttest import t_test

import pandas as pd
import warnings
warnings.filterwarnings("ignore")

def rate_by_event(data,batch_a,batch_b,alpha,input_power):
    """
    :内容：触发指标的用户群体，计算群体在对应指标上的是否存在显著性差异，如充值用户的人均充值，点击下载用户的人均活跃时间等
    :param data:
    :param batch_a:对照组的batchID
    :param batch_b:实验组的batchID
    :param:alpha:浮点数，显著性水平
    :return:
    """
    data = pd.DataFrame(data, dtype='float')
    if data[data['metric'] == 0].empty:
        return t_test(data,batch_a,batch_b,alpha,input_power,ttest_plus_method=True)
    else:
        return {'resultMsg': "Some group are zeros", 'resultCode': 402, 'success': true}