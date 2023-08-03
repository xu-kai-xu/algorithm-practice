# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 07:55:19 2023

@author: xukkk
"""

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
        
        
def levelOrder(root):
    res = []
    node_que = []
    
    if root:
        node_que.append(root)
        
    while node_que:
        size = len(node_que)
        res_level = []
        for _ in range(size):
            node = node_que.pop(0)
            res_level.append(node.val)
            if node.children:
                for child in node.children:
                    node_que.append(child)
                    
        res.append(res_level)
    
    return res
                    
                                      
                    
                    
                    