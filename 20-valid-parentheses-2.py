# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 07:21:21 2023

@author: xuk11

20 有效的括号
"""


def parentheses_match(target, op_stack):
    while op_stack:
        tmp = op_stack.pop()
        if tmp not in ['(', '[', '{']:
            continue
        if target == ')' and tmp == '(':
            return True
        elif target == ']' and tmp == '[':
            return True
        elif target == '}' and tmp == '{':
            return True
        else:
            return False

def isValid(s):
    verify = list(s)
    op_stack = []
    flag = True

    while verify:
        tmp = verify.pop(0)
        if tmp in ['(', '[', '{', ' ']:
            op_stack.append(tmp)
        elif tmp in [')', ']', '}']:
            flag = parentheses_match(tmp, op_stack)

        if not flag:
            return False

    if len(set(op_stack)) == 1 and set(op_stack) == {' '}:
        return True
    elif len(set(op_stack)) == 0:
        return True
    return False
