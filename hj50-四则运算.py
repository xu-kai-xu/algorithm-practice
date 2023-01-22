# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 15:49:45 2022

@author: xuk11

https://www.nowcoder.com/practice/9999764a61484d819056f807d2a91f1e?tpId=37&tqId=21273&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3FtpId%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=

中缀表达式，后缀表达式
https://blog.csdn.net/sgbfblog/article/details/8001651
https://www.bilibili.com/video/BV135411d7cw/?spm_id_from=333.788
https://www.bilibili.com/video/BV1yB4y1179L/?spm_id_from=pageDriver&vd_source=aa068c732e0224662feb747f8c25f344
"""

import re

#raw = '3+2*{1+2*[-4/(8-6)+7]}'
raw = '3*5+8-0*3-6+0+0'
#raw = '5-3+9*6*(6-10-2)'
raw = raw.replace('{', '(')
raw = raw.replace('}', ')')
raw = raw.replace('[', '(')
raw = raw.replace(']', ')')

raw = re.sub(r'[(](-\d)', r'((0\1)', raw)


# 初步切割
def first_cut(strs):
    """切割输入字符串，返回数和运算符的列表"""
    res = []
    num = ''
    opes = ['+', '-', '*', '/', '(', ')']
    for s in strs:
        if s not in opes:
            num += s
        else:
            res.append(num)
            res.append(s)
            num = ''

    if len(num) != 0:
        res.append(num)

    for item in res:
        if len(item) == 0:
            res.remove(item)

    return res


def in_to_suffix(strs_lst):
    """中缀转后缀
    输入为列表，输出为列表
    """
    prior = {'+': 1,
             '-': 1,
             '*': 2,
             '/': 2,
             '(': 0}  # 优先级

    res = []  # 最终结果
    stack = []  # 栈

    for s in strs_lst:
        try:
            num = int(s)  # s is a number
            res.append(s)
        except ValueError:
            # s is an operator 或者括号
            if len(stack) == 0:
                stack.append(s)
            elif s == '(':
                stack.append(s)
            elif s == ')':
                while stack[-1] != '(':
                    #  弹出括号之前的所有元素
                    res.append(stack.pop())
                stack.pop()  # 弹出括号
            else:
                try:
                    while (prior[s] <= prior[stack[-1]]):
                        # 栈中弹出的操作符加到后缀表达式中
                        res.append(stack.pop())
                    stack.append(s)
                except IndexError:
                    stack.append(s)

    while len(stack) != 0:
        res.append(stack.pop())

    return res


def suffix_to_in(suff):
    """后缀转中缀"""
    res = 0
    stack = []
    for s in suff:
        try:
            num = int(s)  # s is a number
            stack.append(s)
        except ValueError:  # 说明是操作符
            tmp1 = int(stack.pop())
            tmp2 = int(stack.pop())
            if s == '*':
                res = tmp2 * tmp1
            if s == '/':
                res = int(tmp2 / tmp1)
            if s == '+':
                res = tmp2 + tmp1
            if s == '-':
                res = tmp2 - tmp1

            stack.append(str(res))  # 将结算结果转换为字符，统一格式
    return int(stack.pop())


atoms = first_cut(raw)

suffix = in_to_suffix(atoms)
res = suffix_to_in(suffix)


