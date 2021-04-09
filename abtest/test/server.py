from flask import Flask
from flask import request
from flask import jsonify
import json

app = Flask(__name__)

import pandas as pd
@app.route('/send_data', methods=['POST'])
def hello_world():
    result = {}
    data = request.get_data().decode('utf-8')
    # print(data, type(data))
    data_list = data.split('&')
    for data in data_list:
        data.find('metric')
    Metric = [data.split('=')[1] for data in data_list if data.find('Metric') != -1]
    UID = [data.split('=')[1] for data in data_list if data.find('UID') != -1]
    Batch = [data.split('=')[1] for data in data_list if data.find('Batch') != -1]
    # UID = request.form.get('UID')
    # Metric = request.form.get('Metric')
    # Batch = request.form.get('Batch')
    result['UID'] = UID
    result['Metric'] = Metric
    result['Batch'] = Batch



    # return jsonify(result)
    # return jsonify(result)
    return jsonify(result)



if __name__ == '__main__':
    app.run()