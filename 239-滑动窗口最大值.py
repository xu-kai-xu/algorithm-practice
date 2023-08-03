# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 07:56:44 2023

@author: xuk11
239-滑动窗口最大值
"""

nums1 = [1,3,-1,-3,5,3,6,7]
k1 = 3

nums2 = [1]
k2 = 1

nums3 = [-7,-8,7,5,7,1,6,0]
k3 = 4


class MonoQueue:
    """
    单调队列
    """
    def __init__(self):
        self.queue = []

    def pop_queue(self, element):
        # element 为窗口移除的元素
        if self.queue[0] == element:
            self.queue.pop(0)

    def push_queue(self, element):
        # element 为窗口需要放入队列中的元素
        while self.queue and self.queue[-1] < element:
            # 当队列尾的元素小于等于element时，弹出队列元素
            self.queue.pop()
        self.queue.append(element)

    def front_queue(self):
        return self.queue[0]


# 使用deque

from collections import deque

class MonoQueue:
    """
    单调队列
    """
    def __init__(self):
        self.queue = deque()

    def pop_queue(self, element):
        # element 为窗口移除的元素
        if self.queue[0] == element:
            self.queue.popleft()

    def push_queue(self, element):
        # element 为窗口需要放入队列中的元素
        while self.queue and self.queue[-1] < element:
            # 当队列尾的元素小于等于element时，弹出队列元素
            self.queue.pop()
        self.queue.append(element)

    def front_queue(self):
        return self.queue[0]


def maxSlidingWindow(nums, k):
    monon_queue = MonoQueue()
    res = []

    # 把前k个元素入栈
    for i in range(k):
        monon_queue.push_queue(nums[i])
    res.append(monon_queue.front_queue())

    for j in range(1, len(nums) - k + 1):
        monon_queue.pop_queue(nums[j - 1])  # 前一个元素pop掉
        monon_queue.push_queue(nums[j + k - 1])
        res.append(monon_queue.front_queue())

    return res


maxSlidingWindow(nums3, k3)
