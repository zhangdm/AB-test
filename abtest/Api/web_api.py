# -*- coding: utf-8 -*-

from abtest.model.ABtest import ABTest
from abtest.model.calculator import cal
from abtest.model.comple_check import comple_check
import json



from flask import Flask,jsonify,request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'welcome to abtest'

@app.route('/abtest/<string:algorithm_name>',methods=['POST','GET'])
def jjabtest_api(algorithm_name):
    data = request.get_data().decode('utf-8')
    data = json.loads(data)

    if algorithm_name == data['algorithm_param']['algorithm_name']:
        alpha = float(data['algorithm_param']['alpha'])
        input_power = float(data['algorithm_param']['input_power'])

        algorithm_name = data['algorithm_param']['algorithm_name']
        Data = data['experiment_param']

        result = ABTest(Data,alpha,input_power,algorithm_name)
        return jsonify(result)
    else:
        return {'resultMsg':"Please check your api link",'resultCode':401,'success':true}


@app.route('/abtest/calculator', methods=['POST', 'GET'])
def calculator():
    data = request.get_data().decode('utf-8')

    data = json.loads(data)

    result = cal(data['original'], data['alpha'], data['power'], data['lift'], data['k'])
    return jsonify(result)


@app.route('/abtest/completeness_check', methods=['POST', 'GET'])
def check():
    data = request.get_data().decode('utf-8')

    data = json.loads(data)

    na = data['na']
    nb = data['nb']
    ratio = data['ratio_a']

    result = comple_check(na, nb, ratio)
    return jsonify(result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)


