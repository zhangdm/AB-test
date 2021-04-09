# -*- coding: utf-8 -*-

import numpy as np
from scipy import stats
from decimal import *
getcontext().prec = 28


def comple_check(na,nb,ratio):
    """
    :内容：完整性检查,
    :方法：基于正态分布的置信区间，假设样本分配到两个实验的概率为都是0.5,
    :param na:对照组的样本量,
    :param nb:实验组的样本量,
    :param ratio:对照组的样本量占比
    :return:0 表示显著性差异，1 表示没有显著性差异
    """

    na,nb = float(na),float(nb)
    ratio_a,ratio_b = float(ratio), 1 - float(ratio)

    sd = np.sqrt(ratio_a*ratio_b/(na+nb))
    z = stats.norm.ppf(1-0.05/2)

    if ratio_a <= ratio_b:
        inter_down = ratio_a - sd*z
        inter_up = ratio_a + sd*z
    else:
        inter_down = ratio_a - sd*z
        inter_up = ratio_a + sd*z

    hat_p = na*1.0000 / (na+nb)
    if hat_p < inter_down or hat_p > inter_up:
        return 0
    return 1