# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 23:20:19 2023

@author: xuk11

203 移除链表元素
https://leetcode.cn/problems/remove-linked-list-elements/
给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足
Node.val == val 的节点，并返回 新的头节点 。

输入：head = [1,2,6,3,4,5,6], val = 6
输出：[1,2,3,4,5]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head, val):
    dummy = ListNode(0, head)
    node = dummy
    #node = head
    while (node.next != None):
        if (node.next.val == val):
            node.next = node.next.next
        else:
            node = node.next

    return dummy.next

m0 = ListNode(6)
m1 = ListNode(5, m0)
m2 = ListNode(4, m1)
m3 = ListNode(3, m2)
m4 = ListNode(6, m3)
m5 = ListNode(2, m4)
m6 = ListNode(1, m5)


res = removeElements(m6, 6)

while (res.next != None):
    print(res.val)
    res = res.next
print(res.val)









