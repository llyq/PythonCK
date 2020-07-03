#!/usr/bin/env python
# @FileName  :concurrency_and_performance.py
# @create by :2020/7/3 1:09
# @author    :liuyuqing

# 并发和性能

# 线程
import time
import threading


# def func1():
#     for i in range(5):
#         time.sleep(1)
#         print('-----------正在做的事情func1-----{}-----------'.format(threading.current_thread()))
#
# def func2():
#     for i in range(6):
#         time.sleep(1)
#         print('-----------正在做的事情func2--------{}--------'.format(threading.current_thread()))

#
# print(time.time())
# func1()
# func2()
# print(time.time())

# 多线程执行多任务
# def main_thread():
#     t1 = threading.Thread(target=func1)
#     t2 = threading.Thread(target=func2, name='th_2')
#     # 开始执行线程1
#     start_time = time.time()
#     # print(t1.getName())
#     print(t1.name)
#     t1.setName('线程1')
#     print(t1.is_alive())
#     t1.start()
#     print(t1.getName())
#     print(t1.is_alive())
#     # 开始执行线程2
#     t2.start()
#     # 让主线程等待子线程执行完后再继续往下执行
#     print(t2.getName())
#     print(threading.enumerate())    # 当前运行的所有线程对象
#     print(threading.active_count()) # 返回当前执行线程的数量(主线程+子线程)
#     t1.join()
#     t2.join()
#     end_time = time.time()
#     print('耗时{}'.format(end_time-start_time))


# 通过继承Thread类来创建线程
import requests
# class RequestThread(threading.Thread):
#     """ 发送requests请求 """
#
#     def __init__(self, url):
#         self.url = url
#         super().__init__()
#
#     def run(self):
#         for i in range(10):
#             res = requests.get(self.url)
#             print('线程：{}---返回的状态码：{}'.format(threading.current_thread(), res.status_code))
#
#
# # 创建5个线程，发起请求
# start_time = time.time()
# for i in range(5):
#     t = RequestThread('http://www.baidu.com')
#     t.start()
#
# # t.join()
# end_time = time.time()
# print('耗时：', end_time-start_time)

# 多线程 全局变量的问题  多线程使用全局变量会造成安全问题

# 全局变量
a = 100
b = [100]

def func1():
    global a
    for i in range(1000000):
        # a += 1
        b[0] += 1
    print('func1--线程1修改完b:', b)


def func2():
    global a
    for i in range(1000000):
        # a += 1
        b[0] += 1
    print('func2--线程2修改完b:', b)


t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)

t1.start()
t2.start()

t1.join()
t2.join()

# print(a)
print(b)

# 作业：10个线程对象，每个线程发送100次请求，计算平均所需耗时
# count = 0
#
# class RequestThread(threading.Thread):
#     """ 发送requests请求 """
#
#     def __init__(self, url):
#         self.url = url
#         super().__init__()
#
#     def run(self):
#         global count
#         for i in range(100):
#             res = requests.get(self.url)
#             count += 1
#             print('线程：{}---第{}次请求--返回的状态码：{}'.format(threading.current_thread(), i, res.status_code))
#
#
# def main():
#     start_time = time.time()
#     # 创建10个线程对象
#     th = [RequestThread('http://www.baidu.com') for j in range(10)]
#     # 遍历线程对象
#     for i in th:
#         # 开始执行
#         i.start()
#     # 遍历线程对象，让主线程等待子线程结束后再往下执行
#     for j in th:
#         j.join()
#     end_time = time.time()
#     print('平均耗时：', (end_time-start_time)/count)
#     print(count)


if __name__ == '__main__':
    # main_thread()
    # ret = RequestThread()
    # print(ret.run())
    # main()
    pass









