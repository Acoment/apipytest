# _*_ coding:UTF-8 _*_
# @time：2022/7/10  15:50
# @Author: 皓雪
# @file: requestUtil.py   
# @Software: PyCharm


import requests
from Conf.yaml_util import cofig_items

class requestUtil():


    def request(self,url,method,headers=None,param =None,content_type=None):

        try:
            url = cofig_items["URL"] + url
            # print(url)
            if method.lower() == 'get':
                result = requests.get(url = url, headers = headers , params = param)
                # print(url,param)
                return result
            elif method.lower() == 'post':
                if content_type == 'application/json':
                    result = requests.post(url = url, headers = headers , json = param)
                    return result
                else:
                    result = requests.post(url = url, headers = headers , params = param)
                    return result
            else:
                print('http method not allowed')
        except Exception as e:
            print(f'请求报错{e}')
if __name__ == '__main__':
    req = requestUtil()
    url = '/tmall/login/doLogin'

    # hearders = {'':'ACBB6CB55C7839A1CEDC6DC3195850C3'}
    method = 'post'
    content_type= 'application/x-www-form-urlencoded'

    param = {'username': 'li14959398','password':'lidehuang2'}

    print(req.request(url,method,param=param,content_type=content_type).text)

