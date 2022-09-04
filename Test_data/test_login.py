# _*_ coding:UTF-8 _*_
# @time：2022/7/10  16:48
# @Author: 皓雪
# @file: test_login.py   
# @Software: PyCharm


import pytest

from Util.ExcelUtil import get_row_values,get_test_data
from Util.requestUtil import requestUtil
from Util.AssertUtil import assert_res

argnames = get_row_values('users.xlsx','login',1)

argvaules = get_test_data('users.xlsx','login')

@pytest.mark.parametrize(argnames,argvaules)
def test_login(project,module,caseid,casename,description,url,method,headers,params,content_type,assertres):
    req = requestUtil()
    # 类型不一致，将字符串修改为 字典
    header = eval(headers) if headers else headers
    params = eval(params) if params else params

    re = req.request(url=url,method=method,headers=header,param=params,content_type=content_type).json()
    # assert re.get('success') == True
    if assertres:
        assert_res(re,assertres)

if __name__ == '__main__':
    pytest.main(['-s','test_login.py'])
