#!/usr/bin/env python
# @FileName  :learn_coroutines.py
# @create by :2020/7/4 15:38
# @author    :liuyuqing
# import time
# import greenlet
# import gevent
# import requests
# import queue
# from gevent import monkey
# monkey.patch_all()    # 一般单线程用
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

# monkey.patch_all()    # 一般单线程用
#
#
# q = queue.Queue()
# for i in range(1000):
#     q.put('http://www.baidu.com')
#
#
# def work():
#     while q.qsize() > 0:
#         url = q.get()
#         requests.get(url)

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
# start_time = time.time()
# g1 = gevent.spawn(work)
# g2 = gevent.spawn(work)
# g3 = gevent.spawn(work)
# g4 = gevent.spawn(work)
# g5 = gevent.spawn(work)
# g6 = gevent.spawn(work)
# g7 = gevent.spawn(work)
# g8 = gevent.spawn(work)
# g9 = gevent.spawn(work)
# g10 = gevent.spawn(work)
# g11 = gevent.spawn(work)
# g12 = gevent.spawn(work)
# g13 = gevent.spawn(work)
# g14 = gevent.spawn(work)
# g15 = gevent.spawn(work)
# g1.join()
# g2.join()
# g3.join()
# g4.join()
# g5.join()
# g6.join()
# g7.join()
# g8.join()
# g9.join()
# g10.join()
# g11.join()
# g12.join()
# g13.join()
# g14.join()
# g15.join()
# # work()  # 耗时： 83.59322452545166
# end_time = time.time()
# print('耗时：', (end_time-start_time))     # 耗时： 41.125406980514526


# 作业：10000个请求，开启2进程，进程中开3线程，线程中开5进程 ===>相当于30个并发

import time
import gevent
import requests
from threading import Thread
from multiprocessing import Process, Queue


# 计算时间的装饰器
def count_time(func):
    """计算函数运行时间的装饰器"""
    def wrapper(*args, **kwargs):
        print('开始执行')
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print('执行结束')
        print("耗时：", (end_time-start_time))
    return wrapper


def gevent_work(q, g_name):
    count = 0
    while not q.empty():
        url = q.get(timeout=0.01)
        requests.get(url)
        gevent.sleep(0.001)
        count += 1
    print('-----协程{}执行了{}个任务'.format(g_name, count))


def process_work(q, p_name):
    thread_list = []
    # 创建10个线程
    for i in range(20):
        t_name = '{} --thread_name---{}'.format(p_name, i)
        print('创建线程{}'.format(t_name))
        t = Thread(target=thread_work, args=(q, t_name))
        thread_list.append(t)
        t.start()
        # 让主线程堵塞，等待子线程
        for t in thread_list:
            t.join()


def thread_work(q, t_name):
    g_list = []
    # 创建20个协程
    for i in range(50):
        g_name = '{}---gevent--{}'.format(t_name, i)
        print('创建协程----{}'.format(g_name))
        g = gevent.spawn(gevent_work, q, g_name)
        g_list.append(g)
    gevent.joinall(g_list)


@count_time
def main():
    # 创建10000个请求消息队列
    q = Queue()

    for i in range(3000):
        q.put('http://www.baidu.com')

    # 开启两个进程处理
    print('队列创建完成, 数量{}'.format(q.qsize()))
    pro_list = []
    for i in range(2):
        p_name = 'process-{}'.format(i)
        print('创建进程{}'.format(p_name))
        p = Process(target=process_work, args=(q, p_name))
        p.start()
        pro_list.append(p)
    # 让主进程等待子进程执行结束后再往下执行
    for p in pro_list:
        p.join()


if __name__ == '__main__':
    main()










