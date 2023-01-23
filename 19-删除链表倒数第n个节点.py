# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 21:47:42 2023

@author: xuk11
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    dummy = ListNode(-1, head)  # dummy node
    fast = slow = dummy
    while (n + 1):
        fast = fast.next
        n -= 1

    while fast:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
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

only_one_node = ListNode(10)

traverse_linked_list(only_one_node)

newhead = removeNthFromEnd(only_one_node, 1)

traverse_linked_list(newhead)
