# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 19:56:06 2022

@author: xuk11
"""

s1 = '()[]{}'
s2 = '['
s3 = '[]'
s4 = '([]{}(()[]))'
s5 = '()[{]}'

def isValid(s):
    bracks = [item for item in s]

    # 创建栈，先放进去一个元素
    queue = []
    queue.append(bracks.pop())

    try:
        while True:
            queue.append(bracks.pop())

            if (queue[-2:] == ['}', '{']) or \
               (queue[-2:] == [']', '[']) or \
               (queue[-2:] == [')', '(']):
                   queue.pop()
                   queue.pop()


    except IndexError:
        pass


    if len(queue) == 0:
        return True
    return False


isValid(s5)

