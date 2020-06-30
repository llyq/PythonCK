#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :data01.py
# @create by :2020/6/30 0:55
# @author    :liuyuqing

import timeit
from collections import namedtuple


# def func():
#     for i in range(10):
#         print(i)

# res = timeit.Timer(func).timeit(100)
# print(res)
# print(timeit.Timer("[1, 2, 4]").timeit(100))
# print(timeit.Timer("(1, 2, 4)").timeit(100))
# res1 = timeit.timeit(func, number=1)
# print(res1)

# # 命名元组
# tuple_1 = ("lili", 20, 'F')
#
# # 设定命名元组类型
# student_info =  namedtuple('info_tuple', ['name', 'age', 'gender'])
#
# tu = student_info(*tuple_1)
# print(tu)
# print(tu.name)
# print(tu.age)
# print(type(tu))
# print(type(student_info))
# print(type(str))
# print(type(list))

# # 字典和集合{}
# # 集合
# li = [1, 2, 4, 1, 3, 1, 2, 5, 5]
# li2 = list(set(li)) # 利用集合对列表去重
# print(li2)
# se = set()  # 空集合
# print(type(se))
# set1 = {1, 2, 3, 1, 2, 3, 5}
# print(set1)

# # 集合添加数据, 属于可变的, 且无序
# set1.add(10)
# se.add("lili")
# se.remove('lili')   # 删除
# se.update((11, 3, 4, 10, 'hh')) # 等同于列表的extend方法
# se.update({3, 4, 5, 6, 'sds'})
# se.update([88, 20])
# print(se)
# se.copy()   # 复制
# print(se)
# se.clear()  # 清空
# print(se)


# # 字典 3.7前是无序的，3.7后是有序的 dict 对象会保持插入时的顺序这个特性
# dict = {}   # 空字典
# print(type(dict))


# -6360066762961334853/散列表的长度  -- 取余
# -842959052585496787/散列表的长度  -- 取余
# 若上述二者一致，则散列冲突

# # 可变与不可变类型：可变不可Hash，不可变可Hash
# # 可变类型：列表、字典； 不可变类型：字符串、元组、数值， 字典可hash的是键
# # set2 = {1, 2, 3, [1, 3]}
# # print(set2)
# set3 = {(1, 3, 5)}
# print(set3)
# set4 = {"fsfdf"}
# print(set4)
# dict_1 = {'name':'lili'}
# set8 = (dict_1)
# print('-------')
# print(set8)
# print(type(set8))
# print(type(dict_1))
# set5 = {{'name':'lili'}}
# print(set5)
# set6 = {{'name':'lili', 'age':20}}
# print(set6)


# urls = []
# for i in range(100):
#     url = 'Page{}'.format(i)
#     urls.append(url)
# print(urls)
#
# # 列表推导式
# urls1= ['pages{}'.format(i) for i in range(100)]
# print(urls1)
#
# # 字典推导式
# dict1 = {i:i+1 for i in range(10)}
# print(dict1)
#
# data_str = "name=lili; age=20"
# print(data_str.split(';'))
# dict_str = {}
# for data in data_str.split(';'):
#     print(data.split('=')[0])
#     print(data.split('=')[1])
#     dict_str[data.split('=')[0]] = data.split('=')[1]
# print(dict_str)
#
# dict_str1 = {data.split('=')[0]:data.split('=')[1] for data in data_str.split(';')}
# print(dict_str1)

# () 生成器表达式
tu = (i for i in range(10)) # 返回生成器对象
print(tu)
# 生成器内部只保留计算规则，不会存储数据，相对列表来讲，节约内存
# print(list(tu))
# print(next(tu))   #全部取出后，不能再次取 ，会抛错StopIteration  需使用的时候再去取值
# print(next(tu))
# print(next(tu))
# print(next(tu))

# #通过yield自定义生成器
# def get_fun():
#     yield 100   # 多个yield 会释放之前的yield，执行后续的代码
#     print('hello')
#     yield 1000
#     yield 10000
#
# res = get_fun() #返回生成器对象
# print(res)
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))


# # 迭代器，生成器是迭代器的一种
# # 可迭代对象：可for循环遍历的都是可迭代对象 内部只实现了 __iter__方法
# li = [1, 2, 4, 5]
#
# li1 = iter(li)  # iter()    __iter__
#
# # 迭代器 内部实现了 __iter__之外，还实现了__next__
# print(next(li1))
# print(type(li1))
# print(next(li))


# 生成器 是迭代器的一种，内部实现了 __iter__,__next__
# 生成器相比迭代器 多了几种方法 send
# tu.send()   # 与生成器进行交互  迭代器-父类、生成器-子类


# def gen():
#     for i in range(1, 5):
#         print('---------')
#         se = yield i
#         print('se的值：', se)
#
#
# g = gen()
# print(next(g))
# # print(next(g))
# # print(g.send(100))
# # print(g.send(200))
#
# # g.close()   # 关闭生成器
# print(next(g))
# # throw 在生成器内部抛出异常，参数-异常类型、异常内容
# g.throw(Exception, "异常")















