# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from scipy import stats

def cal(original, alpha, power, lift, k):
    """
    :样本量计算器：输入对照组转化率,置信水平alpha,统计功效power,提升率lift,实验数k
    :方法：基于用户水平的转化率来计算，依据在样本量很大时，二项分布近似正态分布
    :param original: 原始版本的转化率
    :param alpha: 第一类错误的概率，默认值是0.05
    :param power: 统计功效，默认为0.80
    :param lift: 提升率
    :param k:实验版本个数,k大于或等于2
    :return: 实验所需的样本量
    """
    original = float(original) / 100.000
    lift = float(lift) / 100.000
    alpha = float(alpha) / 100.000
    beta = 1 - float(power) / 100.000
    test_group = original * (1 + lift)
    diff = stats.norm.ppf(1 - alpha / 2) - stats.norm.ppf(beta)
    n = diff ** 2 * (original * (1 - original) + test_group * (1 - test_group)) / (test_group - original) ** 2
    N = float(k) * n
    return {'Num':int(N)}