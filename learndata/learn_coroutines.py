#!/usr/bin/env python
# @FileName  :learn_coroutines.py
# @create by :2020/7/4 15:38
# @author    :liuyuqing
import time
"""
生成器：生成器表达式、函数中使用yield关键字：生成器
"""


def work1():
    for i in range(10):
        print('---work1---{}---'.format(i))
        time.sleep(0.1)
        yield


def work2():
    for i in range(10):
        print('---work2---{}---'.format(i))
        time.sleep(0.1)
        yield


print(type(work2()))
print(type(work1()))

# 通过生成器实现多任务
g1 = work1()
g2 = work2()

while True:
    try:
        next(g1)
        next(g2)
    except StopIteration:
        break


# 协程：微线程
"""
协程本质上是单任务，不存在并行
"""














