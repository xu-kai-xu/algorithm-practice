# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 07:45:12 2023

@author: xukkk
199 二叉树右视图
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right=right
        
        
def rightSideView(root):
    res = []
    node_que = []
    size = 0
    
    if root:
        node_que.append(root)
        
    while node_que:
        size = len(node_que)
        for i in range(size):
            node = node_que.pop(0)
            if node.left:
                node_que.append(node.left)
            if node.right:
                node_que.append(node.right)
            if i == size - 1:
                res.append(node.val)
    
    return res


node1 = TreeNode(1)
node3 = TreeNode(3)
node5 = TreeNode(5)
node8 = TreeNode(8)
node4 = TreeNode(4, node1, node3)
node7 = TreeNode(7, node5, node8)
node6 = TreeNode(6, node4, node7)

t = rightSideView(node6)

