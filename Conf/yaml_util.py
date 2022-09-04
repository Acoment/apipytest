# _*_ coding:UTF-8 _*_
# @time：2022/7/21  22:46
# @Author: 皓雪
# @file: yaml_util.py   
# @Software: PyCharm
import os

import yaml
from dotenv import load_dotenv, find_dotenv

def get_config():
    load_env = load_dotenv(find_dotenv(),override=True)
    if load_env:
        current_env = os.getenv("ENV")
        #读取对应ENV的yaml文件
        file_path = os.path.join(os.path.dirname(__file__),current_env+".yaml")
        with open(file_path,'r',encoding='utf-8') as f:
            return yaml.safe_load(f)
    else:
        raise ModuleNotFoundError(".env 环境配置文件没有找到")

cofig_items = get_config()

if __name__ == '__main__':
    file_path = os.path.join(os.path.dirname(__file__),'dev'+".yaml")
    print(file_path)
