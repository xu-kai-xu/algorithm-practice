# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 21:34:27 2023

@author: xuk11
链表相交
https://leetcode.cn/problems/intersection-of-two-linked-lists-lcci/
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def linked_list_length(head):
    n = 0
    while(head):
        n += 1
        head = head.next
    return n


def getIntersectionNode(headA, headB):
    """
    headA: linked list 1
    headB: linked list 2
    return: the first node where headA and headB intersect
    """
    curA = headA
    curB = headB
    len_headA = linked_list_length(headA)
    len_headB = linked_list_length(headB)
    move = len_headA - len_headB

    if move > 0:
        # headA 比 headB 长
        while move:
            curA = curA.next
            move -= 1
    elif move < 0:
        # headB 比 headA 长
        while -move:
            curB = curB.next
            move += 1
    else:
        pass  # 一样长

    flag = False
    while (curA and curB):
        if curA == curB:
            flag = True
            break
        curA = curA.next
        curB = curB.next

    if not flag:
        return None  # 链表不相交

    return curA





node_5 = ListNode(5)
node_4 = ListNode(4, node_5)
node_3 = ListNode(3, node_4)
node_2 = ListNode(2, node_3)
node_1 = ListNode(1, node_2)
