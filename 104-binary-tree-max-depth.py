# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 23:38:14 2023

@author: xukkk
104 二叉树最大深度
"""

from tree_node import TreeNode


def maxDepth(root):
    depth = 0
    node_que = []

    if root:
        node_que.append(root)
    
    while node_que:
        size = len(node_que)
        
        for _ in range(size):
            node = node_que.pop(0)
            if node.left:
                node_que.append(node.left)
            if node.right:
                node_que.append(node.right)
        depth += 1

    return depth

node1 = TreeNode(1)
node3 = TreeNode(3)
node5 = TreeNode(5)
node8 = TreeNode(8)
node4 = TreeNode(4, node1, node3)
node7 = TreeNode(7, node5, node8)
node6 = TreeNode(6, node4, node7)

t = maxDepth(node1)