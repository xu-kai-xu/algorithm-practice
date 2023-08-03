# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 07:20:30 2023

@author: xukkk
107 层序遍历，返回从叶子节点的层到根节点的层的遍历
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right=right
        

def levelOrderBottom(root):
    res = []
    node_que = []
    
    if root:
        node_que.append(root)
        
    while node_que:
        size = len(node_que)
        res_level = []
        
        while size:
            node = node_que.pop(0)
            res_level.append(node.val)
            if node.left:
                node_que.append(node.left)
            if node.right:
                node_que.append(node.right)
            
            size -= 1
        
        res.append(res_level)

    return res[::-1]
        

node1 = TreeNode(1)
node3 = TreeNode(3)
node5 = TreeNode(5)
node8 = TreeNode(8)
node4 = TreeNode(4, node1, node3)
node7 = TreeNode(7, node5, node8)
node6 = TreeNode(6, node4, node7)

t = levelOrderBottom(node6)


