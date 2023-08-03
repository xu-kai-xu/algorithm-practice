# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 07:56:22 2023

@author: xukkk
637 二叉树层平均值
"""

from tree_node import TreeNode


def averageOfLevel(root):
    node_que = []
    res = []
    
    if root:
        node_que.append(root)
        
    while node_que:
        size = len(node_que)
        total = 0
        
        for _ in range(size):
            node = node_que.pop(0)
            total += node.val
            
            if node.left:
                node_que.append(node.left)
            if node.right:
                node_que.append(node.right)
                
        res.append(total / size)
        
    return res


node1 = TreeNode(1)
node3 = TreeNode(3)
node5 = TreeNode(5)
node8 = TreeNode(8)
node4 = TreeNode(4, node1, node3)
node7 = TreeNode(7, node5, node8)
node6 = TreeNode(6, node4, node7)

t = averageOfLevel(node6)



