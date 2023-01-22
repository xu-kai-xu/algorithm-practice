"""
设计链表
代码随想录上的python代码
https://programmercarl.com/0707.%E8%AE%BE%E8%AE%A1%E9%93%BE%E8%A1%A8.html#%E5%85%B6%E4%BB%96%E8%AF%AD%E8%A8%80%E7%89%88%E6%9C%AC
"""

# 单链表
class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList(object):
    def __init__(self):
        self.head = Node()
        self.size = 0  # 链表长度，便于后续操作

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        cur = self.head.next
        while(index):
            cur = cur.next
            index -= 1
        return cur.val

    def addAtHead(self, val):
        """
        :type index: int
        :rtype: None
        """
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        self.size += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = Node(val)
        cur = self.head
        while(cur.next):
            cur = cur.next
        cur.next = new_node
        self.size += 1

    def ddAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0:
            self.addAtHead(val)
            return
        elif index == self.size:
            self.addAtTail(val)
            return
        elif index > self.size:
            return

        node = Node(val)
        pre = self.head
        while(index):
            pre = pre.next
            index -= 1
        node.next = pre.next
        pre.next = node
        self.size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        pre = self.head
        while(index):
            pre = pre.next
            index -= 1
        pre.next = pre.next.next
        self.size -= 1

