# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 07:37:45 2023

@author: xuk11
150 逆波兰表达式求值
https://leetcode.cn/problems/evaluate-reverse-polish-notation/
当遇到减号时，弹出的第一个操作数是减号后面的那个操作数，而弹出的第二个操作数是减号前面的那个操作数。因此，计算减法时需要注意操作数的顺序。

"""

token1 = ["2","1","+","3","*"]
token2 = ["4","13","5","/","+"]
token3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
token4 = ["18"]

def calculate(num1, num2, token):
    if token == '+':
        return (num1 + num2)
    elif token == '-':
        return (num1 - num2)
    elif token == '*':
        return (num1 * num2)
    elif token == '/':
        return int(num1 / num2)


def evalRPN(tokens):
    oprands = []  # 操作数栈
    res = 0
    for token in tokens:
        if token in ('+', '-', '*', '/'):  # 对于这种不会变的列表，可以用tuple
            num2 = oprands.pop()
            num1 = oprands.pop()
            res = calculate(num1, num2, token)
            oprands.append(res)
        else:
            oprands.append(int(token))

    return oprands[0]


# evalRPN(token3)
evalRPN(['18'])
