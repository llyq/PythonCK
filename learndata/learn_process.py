#!/usr/bin/env python
# @FileName  :learn_process.py
# @create by :2020/7/4 14:34
# @author    :liuyuqing
import time
import requests
# from queue import Queue
from multiprocessing import Process, Queue

# 多进程 进程可做到并行，线程只能做到并发
# 多进程不共享全局变量
a = 100
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# def work1():
#     for i in range(10):
#         global a
#         print('-----------任务1-------{}----'.format(a))
#         a += 1
#         time.sleep(0.5)
#
#
# def work2():
#     for i in range(10):
#         global a
#         print('-----------任务2------{}-----'.format(a))
#         a += 1
#         time.sleep(0.5)

# 进程执行多任务
# 创建两个进程  Windows才有下面个错
# 不在if __name__ == '__main__'下执行会抛错====>相当于 from import，导入时会执行p1 = Process(target=work1) p1.start()

# 多进程间的通讯问题  解决方法：队列？
# 创建一个队列 添加10个任务
# q = Queue()
count = 0

# for i in range(10):
#     q.put('http://www.baidu.com')


def work1(q):
    global count
    # 判断队列中是否有任务
    while q.qsize() > 0:
        url = q.get()
        # 执行任务
        requests.get(url)
        print('--work1正在执行任务---{}-'.format(count))
        count += 1


def work2(q):
    global count
    # 判断队列中是否有任务
    while q.qsize() > 0:
        url = q.get()
        # 执行任务
        requests.get(url)
        print('--work2正在执行任务---{}-'.format(count))
        count += 1


if __name__ == '__main__':
    q = Queue()
    for i in range(10):
        q.put('http://www.baidu.com')
    p1 = Process(target=work1, args=(q, ))
    p2 = Process(target=work2, args=(q, ))

    p1.start()
    p2.start()



