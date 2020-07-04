#!/usr/bin/env python
# @FileName  :learn_process.py
# @create by :2020/7/4 14:34
# @author    :liuyuqing
import time
from multiprocessing import Process

# 多进程 进程可做到并行，线程只能做到并发
# 多进程不共享全局变量
a = 100
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def work1():
    for i in range(10):
        global a
        print('-----------任务1-------{}----'.format(a))
        a += 1
        time.sleep(0.5)


def work2():
    for i in range(10):
        global a
        print('-----------任务2------{}-----'.format(a))
        a += 1
        time.sleep(0.5)

# 进程执行多任务
# 创建两个进程  Windows才有下面个错
# 不在if __name__ == '__main__'下执行会抛错====>相当于 from import，导入时会执行p1 = Process(target=work1) p1.start()


if __name__ == '__main__':
    p1 = Process(target=work1)
    p2 = Process(target=work2)

    p1.start()
    p2.start()


