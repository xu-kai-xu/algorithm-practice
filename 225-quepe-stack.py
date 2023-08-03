# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 07:15:35 2023

@author: xuk11
225 用队列实现栈
"""

class MyStack:

    def __init__(self):
        self.queue_1 = []
        self.queue_2 = []

    def push(self, x: int):
        self.queue_1.insert(0, x)

    def pop(self):
        while len(self.queue_1) > 1:
            self.queue_2.insert(0, self.queue_1.pop())
        res = self.queue_1.pop()
        while len(self.queue_2) > 0:
            self.queue_1.insert(0, self.queue_2.pop())
        return res

    def top(self):
        return self.queue_1[0]

    def empty(self):
        if len(self.queue_1) == 0:
            return True
        return False


obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
param_2 = obj.pop()
param_3 = obj.pop()
param_4 = obj.pop()
param_5 = obj.empty()
