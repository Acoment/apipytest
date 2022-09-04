# _*_ coding:UTF-8 _*_
# @time：2022/7/10  16:22
# @Author: 皓雪
# @file: setting.py   
# @Software: PyCharm


import os
#项目根目录

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 测试数据文件路径
DATA_PATH = os.path.join(BASE_DIR,'Test_data')

print(DATA_PATH)

PATTERN = r'\$\{(.*?)\}'