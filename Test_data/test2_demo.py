# _*_ coding:UTF-8 _*_
# @time：2022/7/17  14:09
# @Author: 皓雪
# @file: test2_demo.py   
# @Software: PyCharm
import os

import pytest,allure

from Util.ExcelUtil import get_row_values,get_test_data
from Util.requestUtil import requestUtil
from Util.AssertUtil import assert_res
from Util.GlobalvalueUtil import global_v

from Util.ParamReplaceUtil import parameters_replace

argnames = get_row_values('users.xlsx','add',1)
argvaules = get_test_data('users.xlsx','add')

@pytest.mark.parametrize(argnames,argvaules)
def test_login(project,module,caseid,casename,description,url,method,headers,params,content_type,assertres,globalvalue
):
    #替换变量
    headers = parameters_replace(headers) if headers else headers
    url = parameters_replace(url)
    params = parameters_replace(params) if params else params

    # 类型不一致，将字符串修改为 字典
    header = eval(headers) if headers else headers
    params = eval(params) if params else params

    re = requestUtil().request(url=url,method=method,headers=header,param=params,content_type=content_type).json()

    # assert re.get('success') == True
    if assertres:
        assert_res(re,assertres)
    if globalvalue:
        global_v.save_globalVariabvle(globalvalue,re)


if __name__ == '__main__':
    pytest.main(['-s','test_login.py'])
