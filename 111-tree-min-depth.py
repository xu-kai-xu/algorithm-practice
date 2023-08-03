# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 23:52:03 2023

@author: xukkk
111 二叉树最小深度
所谓最小深度，是指到最近的叶子节点的深度
"""

from tree_node import TreeNode


def minDepth(root):
    depth = 0
    node_que = []
    if root:
        node_que.append(root)
    
    while node_que:
        size = len(node_que)
        for _ in range(size):
            node = node_que.pop(0)
            if (not node.left) and (not node.right):
                return depth + 1
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

t = minDepth(node6)