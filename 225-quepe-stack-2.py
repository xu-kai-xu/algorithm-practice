# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 07:56:36 2023

@author: xuk11
225 队列实现栈-2
使用一个队列完成
"""

class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int):
        self.queue.insert(0, x)

    def pop(self):
        self._move_queue_element()
        res = self.queue.pop()
        return res

    def top(self):
        return self.queue[0]

    def empty(self):
        if len(self.queue) == 0:
            return True
        return False

    def _move_queue_element(self):
        size = len(self.queue)
        tmp = 0
        while size > 1:
            tmp = self.queue.pop()
            self.queue.insert(0, tmp)
            size -= 1


obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
param_2 = obj.top()
param_3 = obj.pop()
param_4 = obj.top()
param_5 = obj.pop()
param_6 = obj.top()
param_7 = obj.empty()
param_8 = obj.pop()
param_9 = obj.empty()

obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
param_2 = obj.pop()
param_3 = obj.pop()
param_4 = obj.pop()
param_5 = obj.empty()

obj = MyStack()
obj.push(1)
obj.push(2)
param_2 = obj.top()
param_3 = obj.pop()
param_5 = obj.empty()
