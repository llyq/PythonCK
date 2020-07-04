#!/usr/bin/env python
# @FileName  :learn_coroutines.py
# @create by :2020/7/4 15:38
# @author    :liuyuqing
import time
import greenlet
import gevent
import requests
import queue
from gevent import monkey
"""
生成器：生成器表达式、函数中使用yield关键字：生成器
"""


# def work1():
#     for i in range(10):
#         print('---work1---{}---'.format(i))
#         time.sleep(0.1)
#         yield
#
#
# def work2():
#     for i in range(10):
#         print('---work2---{}---'.format(i))
#         time.sleep(0.1)
#         yield
#
#
# print(type(work2()))
# print(type(work1()))
#
# # 通过生成器实现多任务
# g1 = work1()
# g2 = work2()
#
# while True:
#     try:
#         next(g1)
#         next(g2)
#     except StopIteration:
#         break


# 协程：微线程
"""
协程本质上是单任务，不存在并行
协程依赖于线程
协程相对于线程来讲，占用的资源更少(几乎不占用什么资源)
"""


# def work1():
#     for i in range(10):
#         print('---work1---{}---'.format(i))
#         g2.switch()
#         time.sleep(0.1)
#
#
# def work2():
#     for i in range(10):
#         print('---work2---{}---'.format(i))
#         g1.switch()
#         time.sleep(0.1)
#
#
# g1 = greenlet.greenlet(work1)
# g2 = greenlet.greenlet(work2)
#
# g1.switch()


"""
协程：gevent
线程默认不会等待线程执行
协程存在于线程之中，和主线程相当于异步
spawn：开始协程（协程要执行的任务）
join：让线程等待协程执行

协程之间切换的条件：gevent.sleep() 协程耗时等待的情况下才会切换

gevent的程序补丁：gevent.monkey.patch_all()

做并发： 首先考虑协程 》 线程 》 进程
"""

monkey.patch_all()


q = queue.Queue()
for i in range(1000):
    q.put('http://www.baidu.com')


def work():
    while q.qsize() > 0:
        url = q.get()
        requests.get(url)

# def work1():
#     for i in range(10):
#         print('---work1---{}---'.format(i))
#         # gevent.sleep(0.1)
#         # time.sleep(0.01)
#         requests.get('http://www.baidu.com')
#
#
# def work2():
#     for i in range(10):
#         print('---work2---{}---'.format(i))
#         # gevent.sleep(0.1)
#         # time.sleep(0.01)
#         requests.get('http://www.baidu.com')


# 创建两个协程
start_time = time.time()
g1 = gevent.spawn(work)
g2 = gevent.spawn(work)
g3 = gevent.spawn(work)
g4 = gevent.spawn(work)
g5 = gevent.spawn(work)
g6 = gevent.spawn(work)
g7 = gevent.spawn(work)
g8 = gevent.spawn(work)
g9 = gevent.spawn(work)
g10 = gevent.spawn(work)
g11 = gevent.spawn(work)
g12 = gevent.spawn(work)
g13 = gevent.spawn(work)
g14 = gevent.spawn(work)
g15 = gevent.spawn(work)
g16 = gevent.spawn(work)
g17 = gevent.spawn(work)
g18 = gevent.spawn(work)
g19 = gevent.spawn(work)
g20 = gevent.spawn(work)
g21 = gevent.spawn(work)
g22 = gevent.spawn(work)
g1.join()
g2.join()
g3.join()
g4.join()
g5.join()
g6.join()
g7.join()
g8.join()
g9.join()
g10.join()
g11.join()
g12.join()
g13.join()
g14.join()
g15.join()
g16.join()
g17.join()
g18.join()
g19.join()
g20.join()
g21.join()
g22.join()
# work()  # 耗时： 83.59322452545166
end_time = time.time()
print('耗时：', (end_time-start_time))     # 耗时： 41.125406980514526












