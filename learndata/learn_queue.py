#!/usr/bin/env python
# @FileName  :learn_queue.py
# @create by :2020/7/3 23:31
# @author    :liuyuqing
from threading import Thread
import queue

# 三种队列
# 1、先入先出
# q = queue.Queue(3)    # 队列长度最大为3
# # 往队列中添加数据
# q.put(1)
# q.put(3)
# q.put(4)
# # q.put(333, block=False)  # 往队列中添加数据 不等待，队列满了抛错   queue.Full
# # q.put_nowait(55)    # queue.Full
# # 获取数据 获取后不再队列中
# print(q.get())
# print(q.get())
# print(q.get())
# # print(q.get(block=False))   # _queue.Empty
# # print(q.get_nowait())   # _queue.Empty
# # 获取队列中的任务数
# # print(q.qsize()) # 3
# # # 判断队列是否已满
# # print(q.full())
# # # 判断队列是否为空
# print(q.empty())
# q.task_done()
# q.task_done()
# q.task_done()
#
# # join：判断队列中的任务是否执行完毕
# q.join()
# print('join之后的代码')


# 2、后入先出
# q = queue.LifoQueue()
# q.put(1)
# q.put(3)
# q.put(4)
# print(q.get())


# 3、优先级
# q = queue.PriorityQueue()
# q.put(1, 'ddd')
# q.put(444, 'qewqe')
# q.put(4, 'qwdsc')
# print(q.get())
# print(q.get())

# 作业：生产者 消费者
# import time
# q = queue.Queue()
#
# class Producer(Thread):
#     """ 生产者 """
#
#     def run(self):
#         count = 0
#         while True:
#             if q.qsize() < 50:
#                 for i in range(500):
#                     count += 1
#                     goods = '第{}个商品'.format(count)
#                     q.put(goods)
#                     print('生产者:', goods)
#                 time.sleep(1)
#
# class Consumer(Thread):
#     """ 消费者 """
#
#     def run(self):
#         count = 0
#         while True:
#             if q.qsize() > 10:
#                 for i in range(3):
#                     goods = '消费{}个商品'.format(q.get())
#                     print('消费者:', goods)
#             else:
#                 time.sleep(2)
#
# p = Producer()
# p.start()
#
# for i in range(5):
#     c = Consumer()
#     c.start()