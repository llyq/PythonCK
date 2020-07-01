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
# def add(func):
#     def fun(*args, **kwargs):
#         # print('相乘', a * b)
#         return func(*args, **kwargs)
#     return fun

#装饰器 必须return
# @add    # MyClass = add(MyClass)
# class MyClass:
#
#     # def __init__(self):
#     #     pass
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# m = MyClass('lili', 20)
# print(m)

# 定义一个计算函数运行时间的装饰器(计算时间使用time模块实现)
# import time
# def wrapper(func):
#     def count_time(*args, **kwargs):
#         start_time = time.time()
#         func(*args, **kwargs)
#         end_time = time.time()
#         print('函数运行的时间{}'.format(end_time - start_time))
#     return count_time
#
# @wrapper
# def print_index():
#     print('hhhhhh')
#
# print_index()

# 定义装饰器，为多个函数加上认证的功能(用户的账号和密码来源于文件)， 要求登录成功一次，后续的函数都无需再输入用户名和密码

# with open('user.txt') as f:
#     users = eval(f.read())
    # account_info['username'] = users['username']
    # account_info['password'] = users['password']
    # account_info['token'] = users['token']


# def login_check(func):
#     def auth():
#         if users['token'] is False:
#             print('-------------登录页面---------------')
#             user = input('账号:')
#             pd = input('密码:')
#             if (users['username'] == user) and (users['password'] == int(pd)):
#                 users['token'] = True
#                 func()
#         else:
#             func()
#     return auth
#
# @login_check
# def login():
#     print('首页')
#
# @login_check
# def page1():
#     print('page1')
#
# login()
# page1()


# 多个装饰器装饰同一个函数
# import time
# def wrapper(func):
#     def count_time(*args, **kwargs):
#         start_time = time.time()
#         func(*args, **kwargs)
#         end_time = time.time()
#         print('函数运行的时间{}'.format(end_time - start_time))
#     return count_time
#
# with open('user.txt') as f:
#     users = eval(f.read())
#
# def login_check(func):
#     def auth(*args, **kwargs):
#         print('------登录校验的装饰器------------')
#         if users['token'] is False:
#             print('-------------登录页面---------------')
#             user = input('账号:')
#             pd = input('密码:')
#             if (users['username'] == user) and (users['password'] == int(pd)):
#                 users['token'] = True
#                 func(*args, **kwargs)
#         else:
#             func(*args, **kwargs)
#     return auth
#
# # 从上往下执行、从下往上装饰
# @login_check   # 2、count_tim --> func = login_check(func) func -->auth
# @wrapper    # 1、func = wrapper(func) func ==> count_time
# def funcc():
#     time.sleep(2)
#     print('此为需要被装饰器的函数')
#
# funcc()

# # Python类型中三个内置装饰器
# class MyTest():
#
#     def __init__(self):
#         self.name = 'llllll'
#
#     @classmethod    # 被classmethod装饰后，此方法就是类方法  只能在类中调用
#     def add(self):
#         print('add')
#         print(self) # <class '__main__.MyTest'> 类
#
#     @classmethod    # 被classmethod装饰后，此方法就是类方法
#     def add1(cls):
#         print('add1')
#         print(cls) # <class '__main__.MyTest'> 类
#
#     def sub(self):
#         print(self) # <__main__.MyTest object at 0x1070a7ed0> 实例对象
#
#     @staticmethod   # 静态方法 无参数 实例和类均能调用
#     def static():
#         print('静态方法')
#
#     @property   # 设定只读属性 类可调用 ；实例调用后返回值为None 有return时无返回值
#     def read_attr(self):
#         print('这个装饰器装饰完后，该方法可像属性一样被调用')
#         return '18sui'
#
#
# MyTest.add1()
# MyTest.add()
# print('**********************************')
# t = MyTest()
# t.add()
# t.sub()
# t.add1()
# print('------------------------------------')
# t.static()
# MyTest.static()
# print('####################################')
# MyTest.read_attr    # <property object at 0x104b3fd70>
# MyTest.read_attr = '19' #   可对property方法修改，修改后 实例也可对此方法修改
# print(MyTest.read_attr)
# print('---------分隔线-----------')
# t.read_attr
# t.read_attr = '20'  # 单独用实例对此方法修改抛错 AttributeError: can't set attribute
# print(t.read_attr)
# print('---------11分隔线11-----------')
# print(t.name)

# 魔术方法
# class MyClass:
#
#     def __init__(self, name):
#         self.name = name
#
#     def __new__(cls, *args, **kwargs):  # AttributeError: 'NoneType' object has no attribute 'name'
#         print('----new方法-----')
#         # return super().__new__(cls)
#         return object.__new__(cls)
#
#
# m = MyClass('sss')
# print(m.name)

# 单例模式 节约内存、设置全局都可以用的情况
# class MyTest:
#     instance = None # 设   置一个类属性 用来继承该类有没有创建对象
#
#     def __new__(cls, *args, **kwargs):
#         if not cls.instance:
#             cls.instance = object.__new__(cls)
#             return cls.instance
#         else:
#             return cls.instance
#
#
# t1 = MyTest()
# t1.name = 'lili'
# print(id(t1))
#
# t2 = MyTest()
# print(t2.name)
# print(id(t2))

# 装饰器实现单例模式 ？？

# __str__ 和 __repr__方法
# class MyClass(object):
#
#     def __init__(self, name):
#         self.name = name
    #
    # def __str__(self):    #   场景：给用户看 abc
    #     print('------str-----')
    #     # print('sdkdjskskdjsdd') # TypeError: __str__ returned non-string (type NoneType)
    #     return self.name

#     def __repr__(self): # 给程序员用 'abc'
#         print('------repr--------') # TypeError: __repr__ returned non-string (type NoneType)
#         return '<MyClass.object-{}>'.format(self.name)
#
#     def __call__(self, *args, **kwargs):
#         """对象像函数一样调用的时候触发"""
#         print('------call-------')
#
# m = MyClass('rr')
#
# # print(m)    # ------str-----    rr
# # str(m)  # ------str-----
# # format(m)  # ------str-----
#
# # res = repr(m)
# # print(res)  # 没写__str__\__repr__ 返回<__main__.MyClass object at 0x105b289d0>
#
# # __call__方法
#
# def func():
#     print('------------------')
#
# a = '100'
# # a() # TypeError: 'str' object is not callable
# print(a)
# m()

# 单例模式装饰器
# def single(cls):
#     instance = {}
#     def fun(*args, **kwargs):
#         if cls in instance:
#             return instance[cls]
#         else:
#             instance[cls] = cls(*args, **kwargs)
#             return instance[cls]
#     return fun
#
# @single # Test = single(Test)
# class Test:
#     pass
#
# t = Test()

# 通过类实现装饰器 __call__
# class Decorator:
#
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print('-------装饰器中的call-------------')
#         self.func()
#         print('------------装饰器实现了------------------')
#
# @Decorator  # test_01 = Decorator(test_01)
# def test_01():
#     print('--------原来的功能函数----------')
#
# test_01()

# 上下文管理器
# with open('test.txt', 'w+', encoding='utf-8') as f:
#     f.write('加油啊')

# with 后面跟的是一个上下文管理器
#
# class MyOpen:
#     """文件操作的上下文管理器"""
#
#     def __init__(self, file_name, method, encoding='utf-8'):
#         self.file_name = file_name
#         self.method = method
#         self.encoding = encoding
#
#     def __enter__(self):
#         self.f = open(self.file_name, self.method, encoding=self.encoding)   # <_io.TextIOWrapper name='test.txt' mode='r' encoding='cp936'> <_io.TextIOWrapper name='test.txt' mode='r' encoding='utf-8'>
#         return self.f
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(exc_type) # <class 'NameError'>
#         print(exc_tb)   # <traceback object at 0x000001F5A0ABF680>
#         print(exc_val)  # name 'name' is not defined
#         self.f.close()
#
#
# with MyOpen('test.txt', 'r') as f:
#     content = f.read()
#     print(f)
#     print(name)
#     print(content)

# 算数运算
class MyStr:

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data

    def __add__(self, other):
        # print('---触发了add方法---')
        # print('self', self)
        # print('other', other)
        return self.data + other.data

    def __sub__(self, other):
        return self.data.replace(other.data, '')

s1 = MyStr('sf')
s2 = MyStr('qw')
s1+s2
print(s1+s2)
s3 = MyStr('qw33')
print(s3)
print(s3-s2)
print((s1+s2)+s3)   # TypeError: can only concatenate str (not "MyStr") to str





