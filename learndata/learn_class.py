#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: liuyq
@create by: 2020/7/1 4:06 下午
"""

# class MyTest:
#
#     def __init__(self):
#         pass
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

# 多态    Python中多态是伪多态，无类型限制   不修改原来的代码下 写子类继承重写
# class Base:
#
#     def run(self):
#         print('----base--run-----')
#
# class Cat(Base):
#     def run(self):
#         print('-----cat---run------')
#
# class Dog(Base):
#     def run(self):
#         print('-----dog---run------')
#
# class Pig(Base):
#     pass
#
# class MyClass:
#     def run(self):
#         print('-----myclass------')
#
#
# b_obj = Base()
# c_obj = Cat()
# d_obj = Dog()
# p_obj = Pig()
# m = MyClass()
# print(isinstance(c_obj, Base))  # True
# # 子类的对象是属于父类的类型
# print(isinstance(c_obj, Cat))  # True
# print(isinstance(c_obj, Base))  # True
#
# # Python中函数的参数 无类型限制
# #假设func参数需要Base类型  鸭子类型--只需对象实现run方法
# def func(base_obj):
#     base_obj.run()
#
# func(b_obj) # ----base--run-----
# func(c_obj) # -----cat---run------
# func(d_obj) # -----dog---run------
# func(p_obj) # ----base--run-----
# func(m) # -----myclass------

# 元类 新式类(Python3)、旧式类(经典类Python2)
#经典类 继承instance Python2
# class MyClass:
#     pass
# #新式类 继承 object
# class Test(object):
#     pass
#
# t = Test()
# print(type(t))  # <class '__main__.Test'>
# print(type(Test))   # <class 'type'>
# print(type(type))   # <class 'type'>

# type：Python中所有的类都是通过type创建出来的 ---元类
# object：Python3中所有类的顶级父类都是object

# 元类 Python中内置的元类 type动态定义类
# def func(self):
#     print('---------------self-----------')
# # 利用元类直接创建类 是无方法的
# # type创建类需3个参数：类名--字符串、继承的父类--元组、方法+属性--字典
# Test = type('Test', (object, ), {'name': 'lili', '__attr1': 300, 'function1': func})  # <class '__main__.Test'>
# # print(Test)
# print(Test.__dict__)
# test = Test()
# test.function1()    # 动态创建类
# print(Test.__bases__)   # (<class 'object'>,)
#
#
# class Test1:
#     name = '111'
#     __attr1 = 200
#
# print(Test1)    # <class '__main__.Test1'>

# 自定义元类 必须继承type
class MyMetaClass(type):
    """ 将类的所有属性名变成大写 """

    def __new__(cls, name, bases, attr_dict, *args, **kwargs):
        print('----------最基础的自定义元类-----------')
        # return type.__new__(name, bases, attr_dict)
        # new_dict = {}
        # for k, v in attr_dict.items():
        #     new_dict[k.upper()] = v
        for k, v in list(attr_dict.items()):
            attr_dict.pop(k)
            attr_dict[k.upper()] = v
        attr_dict['__slots__'] = ['name', 'age', 'gender']
        return super().__new__(cls, name, bases, attr_dict)

# 通过自定义的元类来创建类
class Test(metaclass=MyMetaClass):
    user_name = 'lili'
    user_age = 99
    user_gender = '男'

# 父类指定元类，子类可继承父类指定的元类
class MyClass(Test):
    pass

# print(type(Test))
# print(Test.user_name)
# print(type(MyClass))
print(Test.__dict__)


