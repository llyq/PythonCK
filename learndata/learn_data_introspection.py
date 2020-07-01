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


class Test:
    attr1 = 100     # 公有属性
    # 私有属性 建议只在内部用
    _attr2 = 200
    __attr3 = 400

class A:
    name = '33334rr'
    __name = 'sddd'

t = Test()
# 类属性可以通过类和实例对象去访问
print(Test.attr1)
print(t.attr1)
# 单下划线的私有属性
print(Test._attr2)
print(t._attr2)
# 双下划线的私有属性，对外不能直接访问，为了保护这个变量 对外改了个名字
# print(Test.__attr3) # AttributeError: type object 'Test' has no attribute '__attr3'
# print(t.__attr3)  # AttributeError: type object 'Test' has no attribute '__attr3'
print(Test.__dict__)
print(Test._Test__attr3)
print(t._Test__attr3)

print('--------------------')
# 私有属性的继承, 可继承
a = A()
# print(a.attr1)
# print(a._attr2)
# print(a.__attr3)
# print(a._Test__attr3)
print(A.__dict__)   # {'__module__': '__main__', 'name': '33334rr', '_A__name': 'sddd', '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}
print(a.__dict__)

# __slots__ 内置属性
# 限制对象的属性;节约内层 定义了slots属性后，该对象
class Base:
    __slots__ = ['name']  # 指定类对象所能绑定的属性不再会自动生辰__dict__

b = Base()
# b.age = 20
b.name = '333ffff'
print(b.name)



