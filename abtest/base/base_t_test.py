# -*- coding: utf-8 -*-

from scipy import stats
import numpy as np
from abtest.base.dfree import dfree
from abtest.base.power import power
from abtest.base.lift_interv import lift_interv


def ttest(dfa,dfb,alpha,input_power,ttest_plus_method = False):
    input_power = float(input_power)
    ## 计算样本量或用户量
    na = dfa.shape[0]
    nb = dfb.shape[0]

    ## 计算每个用户的指标
    metric_a = dfa['metric']
    metric_b = dfb['metric']

    ## 每个用户的指标均值
    avg_a = np.mean(metric_a)
    avg_b = np.mean(metric_b)
    if not ttest_plus_method:
        ## 用户指标的样本方差
        va = np.var(metric_a)
        vb = np.var(metric_b)
    else:
        La = metric_a - avg_a
        Lb = metric_b - avg_a

        va = np.var(La)
        vb = np.var(Lb)

    ## 样本标准差和样本误差
    stda = np.sqrt(va)
    stdb = np.sqrt(vb)
    stdab = np.sqrt(np.square(stda) / (na) + np.square(stdb) / (nb))
    ## 自由度
    Dfree = dfree(stda, stdb, stdab, na, nb)

    ## p值
    pvalue = stats.ttest_ind(metric_a, metric_b, equal_var=False).pvalue
    ## 统计功效
    Power = power(avg_a, avg_b, stdab, alpha, Dfree)

    ## 置信区间下界和上界
    lift, lift_interv_down, lift_interv_up = lift_interv(avg_a, avg_b, stdab, alpha, Dfree)

    result_df = {'A_metric_avg': avg_a, 'B_metric_avg': avg_b, 'lift': lift, 'lift_interv_down': lift_interv_down,'lift_interv_up': lift_interv_up, 'pvalue': pvalue, 'power': Power}
    return result_df