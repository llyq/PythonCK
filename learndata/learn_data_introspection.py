#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :learn_data_introspection.py
# @create by :2020/7/2 0:04
# @author    :liuyuqing

# # 单例模式 节约内存、设置全局都可以用的情况
# class MyTest:
#     __instance = None # 设置一个类属性 用来继承该类有没有创建对象 ;定义成私有属性，防止外部修改
#
#     def __new__(cls, *args, **kwargs):
#         if not cls.__instance:
#             cls.__instance = object.__new__(cls)
#             return cls.__instance
#         else:
#             return cls.__instance
#
#
# t1 = MyTest()
# t1.name = 'lili'
# MyTest.instance = None
# print(id(t1))
#
# t2 = MyTest()
# print(t2.name)
# print(id(t2))


# class Test:
#     attr1 = 100     # 公有属性
#     # 私有属性 建议只在内部用
#     _attr2 = 200
#     __attr3 = 400
#
# class A:
#     name = '33334rr'
#     __name = 'sddd'
#
# t = Test()
# # 类属性可以通过类和实例对象去访问
# print(Test.attr1)
# print(t.attr1)
# # 单下划线的私有属性
# print(Test._attr2)
# print(t._attr2)
# # 双下划线的私有属性，对外不能直接访问，为了保护这个变量 对外改了个名字
# # print(Test.__attr3) # AttributeError: type object 'Test' has no attribute '__attr3'
# # print(t.__attr3)  # AttributeError: type object 'Test' has no attribute '__attr3'
# print(Test.__dict__)
# print(Test._Test__attr3)
# print(t._Test__attr3)
#
# print('--------------------')
# # 私有属性的继承, 可继承
# a = A()
# # print(a.attr1)
# # print(a._attr2)
# # print(a.__attr3)
# # print(a._Test__attr3)
# print(A.__dict__)   # {'__module__': '__main__', 'name': '33334rr', '_A__name': 'sddd', '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}
# print(a.__dict__)
#
# # __slots__ 内置属性
# # 限制对象的属性;节约内层 定义了slots属性后，该对象
# class Base:
#     __slots__ = ['name']  # 指定类对象所能绑定的属性不再会自动生辰__dict__
#
# b = Base()
# # b.age = 20
# b.name = '333ffff'
# print(b.name)

# 实现一个操作mysql的上下文管理(可以自动断开连接)
# import pymysql
# class DB:
#
#     def __init__(self, data_conf):
#         self.conn = pymysql.connect(**data_conf)
#         self.cursor = self.conn.cursor()
#
#     def __enter__(self):
#         return self.cursor
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.cursor.close()
#         self.conn.close()
#
# DATABASES_CONF = dict(
#     host = 'localhost',
#     user = 'root',
#     password = 'mysql',
#     database = 'test',
#     port = 3306,
#     charset = 'uft-8'
# )
#
# with DB(DATABASES_CONF) as cur:
#     cur.execute('select * from students')
#     print(cur.fetchone())

"""
描述__slots__属性的作用，并修改读取Excel类中保存用例的类
1、限制对象属性，指定指定的slots的属性
2、节约内存
"""

class Case:

    __slots__ = ['case_id', 'title', 'url', 'data', 'excepted']

    def __init__(self):
        self.case_id = None
        self.title = None
        self.url = None
        self.data = None
        self.excepted = None
# 存在列表里 列表嵌套字典， 列表嵌套列表，列表存储对象

# 自定义属性访问
# class Test:
#
#     def __init__(self):
#         self.age = 18
#
#     # def __getattr__(self, item):
#     #     """ 当访问属性的时候，若属性不存在(出现AttributeError) 该方法会被触发 --->要么返回异常，要么返回一个(找到的)属性值 """
#     #     print('----------__getattr__------------')
#     #     super().__getattribute__(item)  # AttributeError: 'Test' object has no attribute 'name33'
#     #     return 100
#     #
#     # def __getattribute__(self, item):
#     #     """ 访问属性的时候，第一次触发该方法查找属性 """
#     #     print('------------__getattribute__--------------')
#     #     return 999
#         # super().__getattribute__(item)  # super()可理解为实例
#
#     # def __setattr__(self, key, value):
#     #     """ 在给对象设置属性的时候触发 """
#     #     if key == 'age':    # 当限制某个属性值在类外无法更改，可在此方法进行干扰
#     #         super().__setattr__(key, 18)
#     #     else:
#     #         print('设置属性的时候会触发')
#     #         # print(key, value)
#     #         super().__setattr__(key, value)
#
#     def __delattr__(self, item):
#         """ 删除属性的时候会被触发 """
#         print(item)
#         if item == 'name':
#             pass
#         else:
#             print('----------__delattr__-------------')
#             super().__delattr__(item)
#
#
# t = Test()
# t.name = 10
# t.age = 9999999999
# del t.name  # 删除属性
# print(t.name)
# print(t.age)

#






