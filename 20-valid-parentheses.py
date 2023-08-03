# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 07:45:06 2023

@author: xuk11
20 有效的括号 用到栈


思路：
读到左括号压入栈，读到空格也压入栈。
读到右括号开始弹出，直到弹出对应的左括号。
当输入完后，看栈中剩下的元素，如果有括号，就说明是无效的括号，否则是有效的。

"""

s1 = "()"
s2 = "()[]{}"
s3 = "(]"

s4 = " ( ) ["
s5 = " { ( )  [ ] { }  "
s6 = " ( ] "

s7 = "["
s8= "[["

s9 = "({[)"


def parentheses_match(target, op_stack):
    while op_stack:
        tmp = op_stack.pop()
        if tmp not in ('(', '[', '{'):
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
    stack = []
    flag = True
    for char in s:
        if char in ('(', '[', '{', ' '):
            stack.append(char)
        elif char in (')', ']', '}'):  # 这种不会更改的列表，可以用tuple
            flag = parentheses_match(char, stack)

        if not flag:
            return False

    if len(set(stack)) == 1 and set(stack) == {' '}:
        return True
    elif len(set(stack)) == 0:
        return True
    return False


# parentheses_match(')', ['['])

isValid(s9)
