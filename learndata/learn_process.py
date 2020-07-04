#!/usr/bin/env python
# @FileName  :learn_process.py
# @create by :2020/7/4 14:34
# @author    :liuyuqing
import time
import requests
# from queue import Queue
# from multiprocessing import Process, Queue, Manager

# 多进程 进程可做到并行，线程只能做到并发
# 多进程不共享全局变量
# a = 100
# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


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
# count = 0

# for i in range(10):
#     q.put('http://www.baidu.com')


# def work1(q):
#     global count
#     # 判断队列中是否有任务
#     while q.qsize() > 0:
#         url = q.get()
#         # 执行任务
#         requests.get(url)
#         print('--work1正在执行任务---{}-'.format(count))
#         count += 1
#
#
# def work2(q):
#     global count
#     # 判断队列中是否有任务
#     while q.qsize() > 0:
#         url = q.get()
#         # 执行任务
#         requests.get(url)
#         print('--work2正在执行任务---{}-'.format(count))
#         count += 1

# 进程池
# import os
# import time
# from multiprocessing import Pool


# a = 0


# def work():
#     global a
#     a += 1
#     print('--------任务次数--{}---进程id：{}----'.format(a, os.getpid()))
#     time.sleep(0.5)


# def work1(q):
#     global a
#     # 判断队列中是否有任务
#     url = q.get()
#     # 执行任务
#     requests.get(url)
#     a += 1
#     print('--work1正在执行任务---{}-进程id:{}'.format(a, os.getpid()))



# 创建进程池
# if __name__ == '__main__':
#     # 进程池中的队列
#     q = Manager().Queue()
#     for i in range(100):
#         q.put('http://www.baidu.com')
#
#     pool = Pool(5)
#     for i in range(10):
#         if q.qsize() > 0:
#             pool.apply_async(func=work1, args=(q, ))
#         else:
#             break
#
#     pool.close()
#     pool.join()


# 线程池(自行扩展)


# if __name__ == '__main__':

    # q = Queue()
    # for i in range(10):
    #     q.put('http://www.baidu.com')
    # p1 = Process(target=work1, args=(q, ))
    # p2 = Process(target=work2, args=(q, ))
    #
    # p1.start()
    # p2.start()


# 作业：
import time
import threading
import queue
from multiprocessing import Queue, Manager, Pool

# 线程的队列(只能在一个进程中使用)
q = queue.Queue()
for i in range(100):
    q.put('http://www.baidu.com')
# 可在多个进程间通信
# q1 = Queue()
# for i in range(100):
#     q1.put('http://www.baidu.com')
# 进程池中的队列
# q2 = Manager().Queue()
# for i in range(1000):
#     q2.put('http://www.baidu.com')


# def work():
#     while q.qsize() > 0:
#         url = q.get()
#         requests.get(url)
def work():
    url = q.get()
    requests.get(url)


# def main():
#     start_time = time.time()
#     t1 = threading.Thread(target=work)
#     t2 = threading.Thread(target=work)
#     t3 = threading.Thread(target=work)
#     t1.start()
#     t2.start()
#     t3.start()
#     t1.join()
#     t2.join()
#     t3.join()
#     end_time = time.time()
#     print('耗时：{}'.format(end_time-start_time))

# 线程耗时：2.70173716545105
# 进程池耗时：0.21004629135131836


if __name__ == '__main__':
    # main()
    q2 = Manager().Queue()
    for i in range(1000):
        q2.put('http://www.baidu.com')

    pool = Pool(3)
    start_time = time.time()
    for i in range(q.qsize()):
        pool.apply_async(work, args=(q2, ))
    pool.close()
    pool.join()
    end_time = time.time()
    print('耗时：{}'.format(end_time - start_time))















