# -*- coding: utf-8 -*-



from abtest.model.ttest import t_test

import pandas as pd
import warnings
warnings.filterwarnings("ignore")

def rate_by_event_user(data,batch_a ,batch_b,alpha,input_power):
    """
    :内容：触发事件的用户，计算其每个用户在指标上是否存在显著性差异，如充值群体中每个人充值的分布是否存在差异。
    :param data:数据集
    :param batch_a: 对照组的batch
    :param batch_b: 实验组的batch
    :param:alpha:置信水平
    :return:
    """
    data = pd.DataFrame(data,dtype='float')
    if data[data['metric'] == 0].empty:
        return t_test(data,batch_a,batch_b,alpha,input_power,ttest_plus_method=False)
    else:
        return {'resultMsg': "Some group are zeros", 'resultCode': 402, 'success': true}