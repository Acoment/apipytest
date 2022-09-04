# _*_ coding:UTF-8 _*_
# @time：2022/7/17  15:12
# @Author: 皓雪
# @file: keyrom.py   
# @Software: PyCharm

from faker import Faker

faker = Faker('zh_CN')

def get_name():
    return faker.name()
def get_phone():
    return faker.phone_number()

print(faker.name())
# 'Lucy Cechtelar'
print(faker.phone_number())

print(faker.address())
# '426 Jordy Lodge
#  Cartwrightshire, SC 88120-6700'