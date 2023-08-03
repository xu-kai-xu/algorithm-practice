# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 11:49:06 2022

@author: xuk11
https://www.nowcoder.com/practice/7e124483271e4c979a82eb2956544f9d?tpId=37&tqId=21312&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D2%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=
"""

raw1 = '4 2 K A'
raw2 = 'A A A A'
raw3 = 'B 5 joker 4'
raw4 = 'K Q 6 K'
raw5 = 'J 2 9 2'
raw6 = 'A 2 J 3'

def num_parse(s):
    """输入的字符进行转换，只转换合法字符"""
    try:
        return int(s)
    except ValueError:
        if s == 'A':
            return 1
        elif s == 'J':
            return 11
        elif s == 'Q':
            return 12
        elif s == 'K':
            return 13



def calcu(cal_lst):
    num1 = num_parse(cal_lst[0])
    num2 = num_parse(cal_lst[2])
    if cal_lst[1] == '+':
        return num1 + num2
    if cal_lst[1] == '-':
        return num1 - num2
    if cal_lst[1] == '*':
        return num1 * num2
    if cal_lst[1] == '/':
        return int(num1 / num2)


def guess_24(nums):
    #todo 需要写4个数字的排列出来
    if ('joker' in nums) or ('JOKER' in nums):
        return 'ERROR'

    # 所有可能的数字排列
    nums_arrang = [[nums[0], nums[1], nums[2], nums[3]],
                   [nums[0], nums[1], nums[3], nums[2]],
                   [nums[0], nums[2], nums[1], nums[3]],
                   [nums[0], nums[2], nums[3], nums[1]],
                   [nums[0], nums[3], nums[2], nums[1]],
                   [nums[0], nums[3], nums[1], nums[2]],
                   [nums[1], nums[0], nums[2], nums[3]],
                   [nums[1], nums[0], nums[3], nums[2]],
                   [nums[1], nums[2], nums[0], nums[3]],
                   [nums[1], nums[2], nums[3], nums[0]],
                   [nums[1], nums[3], nums[2], nums[0]],
                   [nums[1], nums[3], nums[0], nums[2]],
                   [nums[2], nums[1], nums[0], nums[3]],
                   [nums[2], nums[1], nums[3], nums[0]],
                   [nums[2], nums[0], nums[1], nums[3]],
                   [nums[2], nums[0], nums[3], nums[1]],
                   [nums[2], nums[3], nums[0], nums[1]],
                   [nums[2], nums[3], nums[1], nums[0]],
                   [nums[3], nums[0], nums[1], nums[2]],
                   [nums[3], nums[0], nums[2], nums[1]],
                   [nums[3], nums[1], nums[2], nums[0]],
                   [nums[3], nums[1], nums[0], nums[2]],
                   [nums[3], nums[2], nums[1], nums[0]],
                   [nums[3], nums[2], nums[0], nums[1]]]


    operands_perm = [['+', '-', '*'], ['+', '-', '/'],
                       ['-', '*', '/'], ['+', '*', '/']]

    # 所有可能的运算符排列
    operands_arrang = [[perm[i], perm[j], perm[k]] for perm in operands_perm  for i in range(3) for j in range(3) for k in range(3)]

    for num in nums_arrang:
        tmp = num.copy()  #临时存储数组
        for item in operands_arrang:
            for i in [0, 1, 2]:
                tmp.insert(2 * i + 1, item[i])

            # 计算
            res = calcu(tmp[:3])
            res = calcu([res, tmp[3], tmp[4]])
            res = calcu([res, tmp[5], tmp[6]])

            if res == 24:
                return ''.join(tmp)
            tmp = num.copy()
    return 'NONE'  # 找不到的情况





nums = raw6.split(' ')
guess_24(nums)


