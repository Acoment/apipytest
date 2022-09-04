# _*_ coding:UTF-8 _*_
# @time：2022/7/17  14:38
# @Author: 皓雪
# @file: ParamReplaceUtil.py   
# @Software: PyCharm

import re
from Conf.setting import PATTERN
from Util.GlobalvalueUtil import global_v
# 随机参数
from Util.keyrom import get_name,get_phone

def parameters_replace(content):
    """
    把参数值替换成实际值
    :param contnet:  http://121231//${id}  --- http://121231//12
    :return:
    """

    keys  = re.findall(PATTERN, content)
    # print(keys)
    for key in keys:
        if key in global_v.globalVars.keys():
            # key 是全局变量 ，利用全局变量替换
            value = global_v.getVars(key)
            content = content.replace('${' + key + '}', str(value))
        else:
            # key 不是全局变量，则作为关键字函数
            value = eval(key)
            content = content.replace('${' + key + '}', str(value))
    return content


if __name__ == '__main__':
    global_v.setVar('id','999')
    content ="'userid':'${id}'"

    print(parameters_replace(content))