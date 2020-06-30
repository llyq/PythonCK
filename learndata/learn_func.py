#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: liuyq
@create by: 2020/6/30 3:27 下午
"""
from collections import Iterable, Iterator, Generator


# def factorial(n):
#      if n == 1:
#          return 1
#      else:
#          return n * factorial(n-1)
#
# print(factorial(2))
#
#
# def fibonacci(n):
#     if (n == 1 or n == 2):
#         return 1
#     else:
#          return  factorial(n-1) + factorial(n-2)
#
# print(fibonacci(2))

# 纯函数 不管在什么时候调用 传入的参数相同 返回的结果一定一致
# print('-----------------')
# 有一对兔子，第三个月起每个月都生一对兔子，小兔子长大到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数是多少（意味着生长期是2）
# 1 2
# 2 2
# 3 2*2  4
# 4 2*2  4
# 5 2*2  4
# 6 2*2*2  8
# 7 2*2*2  8
# 8 2*2*2  8
# 9 2*2*2*2 16
# 10 2*2*2*2 16
# 11 2*2*2*2 16
# 12 2*2*2*2*2 32

# def rabbit_breeding(n):
#     if n < 3:
#         return 2
#     elif n % 3 == 0:
#         return rabbit_breeding(n-1) + rabbit_breeding(n-2)
#     else:
#         return rabbit_breeding(n-1)
#
# result = rabbit_breeding(8)
# print(result)
#
# print('-------------------')
# 小明有100元钱 打算买100本书 A类书籍5元一本，B类书籍3元一本，C类书籍一元两本，请用程序算出小明一共多少种买法(面试笔试题)
# def count(money, books):
#     count_a = int(money/5)
#     count_b = int(money/3)
#     count_c = int(money)
#     counts = 0
#     for a in range(count_a):
#         for b in range(count_b):
#             for c in  range(count_c):
#                 if (a * 5 + b * 3 + c * 0.5) <= money and (c * 2 + a + b) == books:
#                     counts += 1
#     return counts
# print(count(100,100))

# 递归次数的最大限制 Python解释器默认的，1000次
import sys
sys.setrecursionlimit(3000) # 修改递归最大次数
# s = 1
# count = 0
# def count_book(a=0, b=0, c=0):
#     global s
#     s += 1
#     if a*5 + b*3 + c*0.5 <= 100 and a + b + c == 100:
#         global count
#         count += 1
#     if a < int(100/5):
#         if b < int(100/3):
#             if c < (100):
#                 return count_book(a, b ,c+1)
#             else:
#                 return count_book(a, b+1)
#         else:
#             return count_book(a+1)
#
# try:
#     count_book(0, 0, 0)
# except:
#     print(s)

# print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
# # 内置函数
# def func(n):
#     return n * 2

# # filter: 过滤函数，参数：函数、可迭代对象
# li = [1, 2, 4, 5, 6, 3, 44, 33, 1, 4, 2]
# res = filter(func, li)
# print(list(res))
#
# li1 = []
# for i in li:
#     if i > 10:
#         li1.append(i)
# print(li1)
#
# # map: 吧可迭代对象的每个参数拿出，一个一个传到函数中，并将返回结果放至新的对象中
# res2 = map(func, li)
# print(list(res2))   # [2, 4, 8, 10, 12, 6, 88, 66, 2, 8, 4]

# zip: 打包, 以元素最短的为主
# res3 = zip([1, 2, 4], [11, 3, 55, 44, 12], [111, 31, 551])  # [(1, 11, 111), (2, 3, 31), (4, 55, 551)]
# print(res3)
# print(list(res3))
# print(dict(zip([1, 2, 4], [111, 31, 551])))
#
# dict1 =  {'key1':'value1', 'key2':'value2'}
# print(list(dict1.items()))

# 匿名函数
# 适用场景：简单的函数定义（只有一个表达式）
# def func(a, b):
#     return a+b
#
# res4 = lambda a, b: a + b   # 不推荐
# print(res4(1, 3))
# # 运算符优先级
# res5 = (lambda a, b: a + b)(3, 5)  # 推荐即使用即释放
# print(res5)
#
# f = lambda a: a*9   # 不推荐
# print(f(10))
#
# # 用的较多
# li = [1, 2, 4, 5, 6, 3, 44, 33, 1, 4, 2]
# res6 = filter(lambda x: x > 10, li)
# print(res6)
# print(list(res6))
#
# li2 = [(lambda x: x % 5 == 0)(i) for i in range(10)]    # 这种写法比较少见
# li2 = [lambda x: x % 5 == 0 for i in range(10)]
# print(li2)
#
# # 三目运算符
# a = 100
# if a > 100:
#     print(100)
# else:
#     print(22)
#
# print(100) if a > 100 else print(22)    # 比较少用

# 偏函数
# li = [1, 2, 4, 5, 6, 3, 44, 33, 1, 4, 2]
# li1 = [1, 2, 4, 5, 6, 3, 44, 33, 1, 4, 2]
# li2 = [1, 2, 4, 5, 6, 3, 44, 33, 1, 4, 2]
# li3 = [1, 2, 4, 5, 6, 3, 44, 33, 1, 4, 2]
#
# filter(lambda x: x > 10, li)
# filter(lambda x: x > 10, li1)
# filter(lambda x: x > 10, li2)
# filter(lambda x: x > 10, li3)
#
# from functools import partial   # 导入偏函数
# filter2 = partial(filter, lambda x: x > 10)
# res = filter2(li)
# res1 = filter2(li1)
# res2 = filter2(li2)
# res3 = filter2(li3)
# print(list(res))
# print(list(res1))
# print(list(res2))
# print(list(res3))

# 闭包条件：
# 函数中嵌套函数；外层函数返回的是内层嵌套函数; 内层嵌套函数有引用外层的一个非全局变量
# 作用：实现数据的锁定 提高稳定性
# def login():
#     print("登录")
#
#
# def func(num, b):
#     print('----------func调用-------------')
#     # num = 100
#     def count_books():
#         # print(num)
#         print(num, b)
#         print('---------内层函数----------')
#     return count_books
#
# ress = func(100, 'name')
# print(ress.__closure__)

# 开发封闭原则

# def login(func):    # func为要装饰的函数
#     def fun():
#         user = input('请输入账号')
#         pwd = input('请输入密码')
#         username = 'lyq'
#         password = '123'
#         if user == username and pwd == password:
#             func()
#         else:
#             print('账号密码错误')
#     return fun
#
# @login  #将index传入login @login：语法糖   --> index = login（index) index（）
# def index():
#     print("首页 源函数")
#
# # index --> fun
# print(index)    # <function login.<locals>.fun at 0x00000260586425E0>
# # 传进去的index在closure中
# print(index.__closure__)    # (<cell at 0x00000260583B89D0: function object at 0x0000026058642550>,)
# # index()
#

# 带参数的装饰器
# def add(func):
#     def fun(a, b):
#         print('相乘', a * b)
#         func(a, b)
#     return fun
#
# @add
# def add_num(a, b):
#     print('相加',a+b)
#
# add_num(1, 4)

#通用装饰器
# def add(func):
#     def fun(*args, **kwargs):
#         # print('相乘', a * b)
#         func(*args, **kwargs)
#     return fun
#
# @add
# def add_num(a, b):
#     print('相加',a+b)
#
# @add
# def index():
#     print("首页 源函数")
#
# add_num(1, 3)
# index()
#
# def fun1(*args):
#     print(args)
# fun1([2, 4])

# 装饰器装饰类  可用全局变量，不一定严格遵守闭包
def add(func):
    def fun(*args, **kwargs):
        # print('相乘', a * b)
        return func(*args, **kwargs)
    return fun

#装饰器 必须return
@add    # MyClass = add(MyClass)
class MyClass:

    # def __init__(self):
    #     pass

    def __init__(self, name, age):
        self.name = name
        self.age = age

m = MyClass('lili', 20)
print(m)

# 用类装饰器
# 多个装饰器装饰同一个函数
# python中类里面的三个内置装饰器








