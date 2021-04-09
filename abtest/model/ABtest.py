# -*- coding: utf-8 -*-

from abtest.model.rate_by_event import rate_by_event
from abtest.model.chi_test import *
from abtest.model.wilcoxon_test import rank_sum_test
from abtest.model.fish_exact import fisher_test
from abtest.model.mannwhit_test import U_test
from abtest.errors.handlers import data_checking
from abtest.model.anova_one_way import anova_test
from abtest.model.ttest import t_test
from abtest.model.rate_by_event_user import rate_by_event_user


def ABTest(data,alpha,input_power,algorithm_name):
    """
    :param data:
    :param batcha:
    :param batchb:
    :param alpha
    :param type:
    :return:
    """
    N_base_metrics = len(data['batch_base']['user_metrics'])
    N_comparisons = len(data['batch_comparisons'])
    result = {}
    for i in range(1, N_base_metrics + 1):
        for j in range(0, N_comparisons):
            k = j + 1
            metrics_comparison = 'metric' + '_' + str(i) + '_' + 'comparison' + '_' + str(k)

            user_metric = 'user_metrics' + '_' + str(i)
            batch_comparison = 'batch_comparisons' + '_' + str(k)

            base = pd.DataFrame({'metric': data['batch_base']['user_metrics'][user_metric],'batch':1})
            comparison = pd.DataFrame({'metric':data['batch_comparisons'][j][batch_comparison]['user_metrics'][user_metric],'batch':2})

            Data_concat = pd.concat([base,comparison],axis = 0)
            Data = pd.DataFrame(Data_concat, dtype='float')
            batcha = float(1)
            batchb = float(2)

            Data = data_checking(Data, batcha, batchb)

            if Data is None:
                return {'resultMsg':
                            "Some null values or some group is zeros",
                        'resultCode': 402,
                        'success': true
                        }
            if not algorithm_name:
                return {'resultMsg':
                            "Do not give a algorithm for the ab test",
                        'resultCode': 403,
                        'success': true
                        }

            result_temp = choice_algorithm(Data, batcha, batchb, alpha, input_power,algorithm_name)

            result[metrics_comparison] = result_temp
    return result







def choice_algorithm(Data,batcha,batchb,alpha,input_power,type):
    if type == 'conv':
    # 转化率
        result = t_test(Data, batcha, batchb, alpha, input_power, ttest_plus_method=False)
    elif type == 't_avg_dist':
    # 某个阶段的指标分布的T检验
        result = t_test(Data,batcha,batchb,alpha,input_power,ttest_plus_method=False)
    elif type == 't_event_dist':
    # 某个阶段，触发指标的分布的T检验
        result = rate_by_event_user(Data, batcha, batchb, alpha, input_power)
    elif type == 'avg_t':
    # 某阶段的均值
        result = t_test(Data, batcha, batchb, alpha, input_power, ttest_plus_method=True)
    elif type == 'avg_event_t':
    # 某个阶段触发指标的均值
        result = rate_by_event(Data, batcha, batchb, alpha, input_power)
    # 卡方检验
    elif type == 'chi_test':
        result = chi_test(Data, batcha, batchb, alpha, input_power)
    elif type == 'rank_sum_test':
        result = rank_sum_test(Data, batcha, batchb, alpha, input_power)
    elif type == 'fisher_test':
        result = fisher_test(Data, batcha, batchb, alpha, input_power)
    elif type == 'u_test':
        result = U_test(Data, batcha, batchb, alpha, input_power)
    elif type == 'anova_test':
        result = anova_test(Data, batcha, batchb, alpha, input_power)
    else:
    # 超出界限了，type设置错误
        return {'resultMsg': "Do not give a algorithm for the ab test", 'resultCode': 403, 'success': true}

    return result