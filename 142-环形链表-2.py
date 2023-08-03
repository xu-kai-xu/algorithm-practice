# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 06:40:21 2023

@author: xuk11
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def nodeCatchUp(head):
    fast = slow = head
    while True:
        if (fast and fast.next):
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return slow
        else:
            return None


def detectCycleEntry(head, node_catch_up):
    fast = head
    slow = node_catch_up
    if fast == slow:
        return fast
    while (fast and slow):
        fast = fast.next
        slow = slow.next
        if fast == slow:
            break
    return slow


def detectCycle(head):
    node_catch_up = nodeCatchUp(head)
    cycle_entry = detectCycleEntry(head, node_catch_up)
    return cycle_entry


# ---------------------------------
# test
def traverse_linked_list(head):
    test = head
    while test:
        print(test.val)
        test = test.next


# node_5 = ListNode(5)
# node_4 = ListNode(-4)
# node_3 = ListNode(0, node_4)
# node_2 = ListNode(2, node_3)
# node_1 = ListNode(3, node_2)
# node_4.next = node_2

node_2 = ListNode(2)
node_1 = ListNode(1, node_2)
node_2.next = node_1

node_4 = ListNode(-4)

traverse_linked_list(node_1)

node_catch_up = nodeCatchUp(node_1)
cycle_entry = detectCycleEntry(node_1, node_catch_up)
