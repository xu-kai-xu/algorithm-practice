# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 07:11:35 2023

@author: xuk11
202 快乐数
ps 听到这个名字 我可一点都不快乐
"""
num1 = 19
num2 = 2


def get_digit(num):
    res = []
    while (num // 10):
        res.append(num % 10)
        num = num // 10
    res.append(num)

    return res

def calc_square_sum(num):
    num_lst = get_digit(num)
    square_itr = map(lambda x: x ** 2, num_lst)
    res = sum(square_itr)
    return res

def is_happy_num(num):
    square_sums = dict()
    tmp = num
    while True:
        tmp = calc_square_sum(tmp)
        if tmp == 1:
            return True
        elif square_sums.get(tmp) is None:
            square_sums[tmp] = 1
        else:
            return False

is_happy_num(19)

i = 0
num = 2
ret = []
while (i < 20):
    ret.append(calc_square_sum(num))
    num = ret[-1]
    i += 1
