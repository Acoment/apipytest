# _*_ coding:UTF-8 _*_
# @time：2022/7/10  11:08
# @Author: 皓雪
# @file: test_param.py
# @Software: PyCharm

import pytest


@pytest.fixture()
def except_value():
    return 1
#
# # 如果argnames 只包含一个参数，那么，argvaules 的迭代返回的元素可以是具体的值
# @pytest.mark.parametrize(('input'),[1,2,3])
# def test_single(input):
#     print(f'{input}')
#     assert input+1 == 3
#
# # 如果argnames 只包含多个参数，那么，argvaules 的迭代返回的元素可以是具体的值
# @pytest.mark.parametrize(('input','except_value'),((1,2),(2,1),[3,1]))
# def test_more(input,except_value):
#     print(f'{input}-{except_value}')
#     assert input+1 == except_value


# # 一个函数标记多个paramertrize 标记
# @pytest.mark.parametrize('test_input',[7,8,9])
# @pytest.mark.parametrize('test_output,excepted',[(1,2),[2,1]])
# def test_mulit(test_input,test_output,excepted):
#     print(test_input,test_output,excepted)

# indirect = True ,会把argnames 当做函数执行，并且，将argvalues
@pytest.fixture()
def getuser(request):
    user = request.param
    print(f'获取的用户为：{user}')
    return user

data = ['cc','xiaohu']

@pytest.mark.parametrize('getuser',data,indirect=True)
def test_user(getuser):
    print(f'{getuser}')

print(ord('A'))