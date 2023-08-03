# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 19:52:37 2022

@author: xuk11

代码随想录之链表

"""

class ListNode:
    """
    链表节点类
    """

    def __init__(self, data, point_to):
        # data 数据
        # point_to 指向另一个链表节点
        self.data = data
        self.point_to = point_to

    def is_head(self):
        # 头节点 这里默认头结点的数据是header
        if self.data == 'head':
            return True
        return False

    def is_end(self):
        # 尾节点
        if self.point_to is None:
            return True
        return False

    def traverse(self):
        # 从某个节点遍历链表，直到尾节点
        res = [self.data]
        tmp = self.point_to
        while tmp.point_to is not None:
            res.append(tmp.data)
            tmp = tmp.point_to
        res.append(tmp.data)
        res.append(None)
        return res

    def findNext(self):
        # 查找下一个节点
        return self.point_to



# 链表相关操作

def addNode(self, data):
    # 插入节点
    pass


def deleteNode(head, val):
    # 在以head为头结点的链表中，删除值等于data的链表节点
    # 删除链表的时候，得多看一步，直接查看当前节点的下一个节点
    # 如果查看当前节点，那么久没办法返回去找上一个节点了（在单向链表中）
    node = head
    while node.point_to.data is not None:
        if node.point_to.data == val:
            print(node.point_to.data)
            node.point_to = node.point_to.point_to
        else:
            node = node.point_to

        return node.traverse()





# 链表要倒着添加
t8 = ListNode(6, None)
t7 = ListNode(5, t8)
t6 = ListNode(4, t7)
t5 = ListNode(3, t6)
t4 = ListNode(6, t5)
t3 = ListNode(2, t4)
t2 = ListNode(1, t3)
head = ListNode('head', t2)

# 遍历
head.traverse()
t2.traverse()

# 删除元素
deleteNode(head, 6)




