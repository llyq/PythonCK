#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :data01.py
# @create by :2020/6/30 0:55
# @author    :liuyuqing

import timeit


def func():
    for i in range(10):
        print(i)

res = timeit.Timer(func).timeit(100)
# print(res)
# print(timeit.Timer("[1, 2, 4]").timeit(100))
# print(timeit.Timer("(1, 2, 4)").timeit(100))
res1 = timeit.timeit(func, number=1)
print(res1)