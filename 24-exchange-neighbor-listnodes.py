# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 10:24:07 2023

@author: xuk11
https://leetcode.cn/problems/swap-nodes-in-pairs/
https://programmercarl.com/0024.%E4%B8%A4%E4%B8%A4%E4%BA%A4%E6%8D%A2%E9%93%BE%E8%A1%A8%E4%B8%AD%E7%9A%84%E8%8A%82%E7%82%B9.html#_24-%E4%B8%A4%E4%B8%A4%E4%BA%A4%E6%8D%A2%E9%93%BE%E8%A1%A8%E4%B8%AD%E7%9A%84%E8%8A%82%E7%82%B9
24 两两交换链表中节点的值
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head):
    dummy = ListNode(-1, head)  # 虚拟头节点
    cur = dummy

    while cur.next.next and cur.next:
        # 删除 temp 节点
        temp = cur.next
        cur.next = cur.next.next

        # 移动当前节点到新的节点
        cur = cur.next

        # 添加 temp 节点
        temp.next = cur.next
        cur.next = temp

        # 移动当前节点到新的节点
        cur = cur.next

    return dummy.next

#---------------------------------
# test
def traverse_linked_list(head):
    test = head
    while test:
        print(test.val)
        test = test.next

node_5 = ListNode(5)
node_4 = ListNode(4, node_5)
node_3 = ListNode(3, node_4)
node_2 = ListNode(2, node_3)
node_1 = ListNode(1, node_2)

traverse_linked_list(node_1)
new_node = swapPairs(node_1)
traverse_linked_list(new_node)
