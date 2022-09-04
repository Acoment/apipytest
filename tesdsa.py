# _*_ coding:UTF-8 _*_
# @time：2022/7/10  9:12
# @Author: 皓雪
# @file: tesdsa.py.py   
# @Software: PyCharm
import os

from jsonpath import jsonpath



a = {'username': 'li14959398', 'password': 'lidehuang2'}

dic = {
    'username':'cc',
    'data': {
        "name":"dd",
        "age":15
    },
    'hobbies':[
        {"num1":1},
        {"num2":2}
    ]
}

print(a.get('password'))
print(a['username'])

res = jsonpath(dic,"$.username")[0]
print(res)
res = jsonpath(dic,"$.hobbies[1].num2")[0]
print(res)
res = jsonpath(dic,"$.data.age")[0]
print(res)

#
# # 环境变量切换
# import Conf
# print(os.getenv('url'))
# print(os.getenv('username'))

from Conf.yaml_util import cofig_items
print(cofig_items['URL'])

print('None')
print(type(None))