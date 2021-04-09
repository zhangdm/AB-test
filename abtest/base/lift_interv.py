# -*- coding: utf-8 -*-
from scipy import stats

def lift_interv(avg_a,avg_b,stdab,alpha,dfree):
    t_1_alpha_2 = stats.t.ppf(1 - alpha / 2, dfree)
    interv_down = avg_b - avg_a - t_1_alpha_2 * stdab
    interv_up = avg_b - avg_a + t_1_alpha_2 * stdab

    ## 提升率，提升率下界和上界
    lift = (avg_b - avg_a) / avg_a
    lift_interv_down = interv_down / avg_a
    lift_interv_up = interv_up / avg_a
    return lift,lift_interv_down,lift_interv_up