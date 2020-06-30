#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: liuyq
@create by: 2020/6/30 3:27 下午
"""

def factorial(n):
     if n == 1:
         return 1
     else:
         return n * factorial(n-1)

print(factorial(2))


def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
         return  factorial(n-1) + factorial(n-2)

print(fibonacci(2))

# 纯函数 不管在什么时候调用 传入的参数相同 返回的结果一定一致
print('-----------------')
# 有一对兔子，第三个月起每个月都生一对兔子，小兔子长大到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数是多少（意味着生长期是2）
# 1 2
# 2 2
# 3 2*2  4
# 4 2*2  4
# 5 2*2  4
# 6 2*2*2  8
# 7 2*2*2  8
# 8 2*2*2  8
# 9 2*2*2*2 16
# 10 2*2*2*2 16
# 11 2*2*2*2 16
# 12 2*2*2*2*2 32

def rabbit_breeding(n):
    if n < 3:
        return 2
    elif n % 3 == 0:
        return rabbit_breeding(n-1) + rabbit_breeding(n-2)
    else:
        return rabbit_breeding(n-1)

result = rabbit_breeding(8)
print(result)

print('-------------------')
# 小明有100元钱 打算买100本书 A类书籍5元一本，B类书籍3元一本，C类书籍一元两本，请用程序算出小明一共多少种买法(面试笔试题)
def count(money):
    count_a = int(money/5)
    count_b = int(money/3)
    counts = 0
    for a in range(count_a+1):
        for b in range(count_b+1):
            money_c = money - count_a - count_b
            if money_c <= 100:
                counts += 1
    return counts

# 内置函数





