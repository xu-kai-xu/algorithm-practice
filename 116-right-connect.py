# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 23:11:58 2023

@author: xukkk
116 填充每个节点的下一个右侧节点
"""

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
        

def connect(root):
    res = []
    node_que = []
    
    if root:
        node_que.append(root)
        
    while node_que:
        size = len(node_que)
        node_level = []
        
        for _ in range(size):
            node = node_que.pop(0)
            node_level.append(node)  # 把每层的节点取出，之后赋指针
            if node.left:
                node_que.append(node.left)
            if node.right:
                node_que.append(node.right)
        
        if len(node_level) == 1:
            node_level[0].next = None
        else:
            for i in range(len(node_level) - 1):
                node_level[i].next = node_level[i + 1]
            node_level[i + 1].next = None
    
    return root
            