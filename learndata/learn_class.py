#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: liuyq
@create by: 2020/7/1 4:06 下午
"""

class MyTest:

    def __init__(self):
        pass

    @classmethod    # 被classmethod装饰后，此方法就是类方法  只能在类中调用
    def add(self):
        print('add')
        print(self) # <class '__main__.MyTest'> 类

    @classmethod    # 被classmethod装饰后，此方法就是类方法
    def add1(cls):
        print('add1')
        print(cls) # <class '__main__.MyTest'> 类

    def sub(self):
        print(self) # <__main__.MyTest object at 0x1070a7ed0> 实例对象

    @staticmethod   # 静态方法 无参数 实例和类均能调用
    def static():
        print('静态方法')

    @property   # 设定只读属性 类可调用 ；实例调用后返回值为None 有return时无返回值
    def read_attr(self):
        print('这个装饰器装饰完后，该方法可像属性一样被调用')
        return '18sui'



