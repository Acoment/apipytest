# _*_ coding:UTF-8 _*_
# @time：2022/7/17  10:20
# @Author: 皓雪
# @file: AssertUtil.py   
# @Software: PyCharm

from jsonpath import jsonpath

def assert_res(response,assertres):
    """
    根据assertres 进行断言
    :param response:
    :param assertres:
    :return:
    """
    for tme_assres in assertres.split(";"):
        except_value = tme_assres.split("=")[1]
        actual_expr = tme_assres.split("=")[0]
        actual_value = jsonpath(response,actual_expr)[0]

        assert str(actual_value) == except_value