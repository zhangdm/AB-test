# -*- coding: utf-8 -*-

def split_batch(data,batch_a,batch_b):
    """
    :内容: 根据batch_id将数据划分为对照组、实验组数据集，用batch_a表示对照组，batch_b表示是实验组
    :param data: 测试项目的数据
    :param:batch:区分实验组的“字段”名称
    :param batch_a: 对照组的batch号
    :param batch_b: 实验组的batch号
    :return: 对照组、实验组的数据
    """
    batch_a = float(batch_a)
    batch_b = float(batch_b)
    dataa = data[data['batch'] == batch_a]
    datab = data[data['batch'] == batch_b]
    return dataa,datab