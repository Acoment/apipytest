# _*_ coding:UTF-8 _*_
# @time：2022/7/17  13:54
# @Author: 皓雪
# @file: GlobalvalueUtil.py   
# @Software: PyCharm

from jsonpath import jsonpath

class GlobalVaribales:

    #实现单态
    __intance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__intance:
            cls.__intance = super(GlobalVaribales, cls).__new__(cls)
        return cls.__intance

    def __init__(self):
        self.globalVars = {}

    def setVar(self,key,value):
        """
        添加全局变量
        :param key:
        :param value:
        :return:
        """
        self.globalVars[key] = value


    def getVars(self,key):
        """
        获取某个全局变量值
        :param key:
        :return:
        """
        return self.globalVars[key]

    def save_globalVariabvle(self,globalvalue,res):
        """
        根据excle中的globalvalue的值，来保存全局变量
        :return:
        """
        for tmp_global in globalvalue.split(';'):
            tmp_global = tmp_global.strip()
            key = tmp_global.split('=')[0].strip()
            value = jsonpath(res,tmp_global.split('=')[1].strip())[0]
            # print(tmp_global)
            # print(value)
            self.setVar(key,value)


global_v = GlobalVaribales()
# global_v.setVar('id','999')
# print(global_v.globalVars['id'])
