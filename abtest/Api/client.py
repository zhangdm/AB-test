# -*- coding: utf-8 -*-

import requests
import json
import numpy as np
import pandas as pd

Data = {"experiment_param": {
    "batch_base": {
        "user_list": [1,2,3,4,5],
        "user_metrics": {
            "user_metrics_2": [1,2,3,9,10],
            "user_metrics_1": [1,2,3,3,6]
        }
    },
    "batch_comparisons": [
        {
            "batch_comparisons_1": {
                "user_list": [1,2,3],
                "user_metrics": {
                    "user_metrics_2": [1,2,3],
                    "user_metrics_1": [1,2,3]
                }
            }
        },
        {
            "batch_comparisons_2": {
                "user_list": [1,2,3],
                "user_metrics": {
                    "user_metrics_2": [1,2,3],
                    "user_metrics_1": [1,2,3]
                }
            }
        }
    ]
},
    "algorithm_param": {
        "alpha": 0.05,
        "algorithm_name": "anova_test",
        "input_power": 0.8
    }

}


Data = json.dumps(Data)



r = requests.post('http://127.0.0.1:3000/abtest/anova_test',data = Data)
print (r.content)





data_check = {'na':300,'nb':550,'ratio_a':0.45}
#
Data_check = json.dumps(data_check)
r_check = requests.post('http://127.0.0.1:3000/abtest/completeness_check',data = Data_check)
print (r_check.content)
#
#
data_calculator = {'original':30, 'alpha':5, 'power':80, 'lift':20, 'k':6}

data_calculator = json.dumps(data_calculator)


r_calculator = requests.post('http://127.0.0.1:3000/abtest/calculator',data = data_calculator)
print (r_calculator.content)