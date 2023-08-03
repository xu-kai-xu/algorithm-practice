# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 07:30:56 2023

@author: xuk11
232 用栈实现队列
"""

class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int):
        self.stack_in.append(x)

    def pop(self):
        self.stack_move()
        return self.stack_out.pop()


    def peek(self):
        self.stack_move()
        return self.stack_out[-1]

    def empty(self):
        if not self.stack_in and not self.stack_out:
            return True
        return False

    def stack_move(self):
        if self.stack_out:
            pass
        else:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())


obj = MyQueue()
obj.push(1)
obj.push(2)
param_3 = obj.peek()
param_2 = obj.pop()
param_4 = obj.empty()
