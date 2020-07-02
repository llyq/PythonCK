#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :learn_model_orm.py
# @create by :2020/7/2 23:53
# @author    :liuyuqing

from django.db import models

# models.Model()

# class ModelBase(type):    # 来源于models.Model()
#     """Metaclass for all models."""
#     def __new__(cls, name, bases, attrs, **kwargs):
#         super_new = super().__new__
#
# # 等同于 f =  t.func 而不是 t.func(), 加()代表调用
# class Test:
#     def func(self):
#         pass
#
# t = Test()
# f =  t.func

from learndata.failed import BaseFiled, InitFiled, CharFiled, BoolFiled


# 利用元类实现模型类
class FieldMetaClass(type):
    """ 模型类的元类 """

    def __new__(cls, name, bases, dicts, *args, **kwargs):
        if name == 'BaseModel':
            return super().__new__(cls, name, bases, dicts)
        else:
            table_name = name.lower()  # 将类名转换成小写
            fields = {}  # 定义一个空字典 用来存放模型类字段和数据表中字段的对应关系
            for k, v in dicts.items():  # 遍历所有的属性
                if isinstance(v, BaseFiled):  # 判断属性值是否是字段类型的
                    fields[k] = v
            dicts['t_name'] = table_name
            dicts['fields'] = fields
            return super().__new__(cls, name, bases, dicts)


class BaseModel(metaclass=FieldMetaClass):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)  # 设置属性--对象、属性、属性值   遍历出所有关键字参数并且对对象进行属性设置
            # print(self)
            # print(k)
            # print(v)

    def save(self):
        """ 保存一条数据，生成一条SQL语句 """
        # 获取表名
        t_name = self.t_name
        # 获取字段名称
        fields = self.fields
        # 创建一个字典用例存储键值对
        fields_dict = {}
        # 获取字段对应的值
        for k in fields.keys():
            fields_dict[k] = getattr(self, k)
        # 生成对应的SQL语句
        sql = 'INSERT INTO {} VALUES {}'.format(t_name, tuple(fields_dict.values()))
        print(sql)


class User(BaseModel):
    """ 用户模型类 """
    username = CharFiled()
    pwd = CharFiled()
    age = InitFiled()
    live = BaseFiled()


class Order(BaseModel):
    """ 订单模型类 """
    id = InitFiled()
    money = InitFiled()


xm = User(username='小明', age=18, pwd='123', live=True)
print(xm.username)
print(xm.__dict__)
xm.save()
# xm = Order(id=1, money=500)
# print(xm.id)
# xm = User()
# xm.name = '小明'
# xm = User()
# xm.name = '小八'
# print(xm.name)
# print(xm.name)
print(User.fields)  # 'age': <learndata.failed.InitFiled object at 0x00000282E0233430>
print(User.t_name)
