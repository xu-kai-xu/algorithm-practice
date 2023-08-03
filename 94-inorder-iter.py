# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 07:52:37 2023

@author: xukkk
94 中序遍历 迭代法
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

# def inorderTraversal(root):
#     res = []
#     node_stack = []
    
#     node_stack.append(root)  # 先把根节点放进数组
    
#     while True:
#         node = node_stack[-1]
#         if not node:
#             break
#         if node.right:
#             node_stack.pop()
#             node_stack.append(node.right)
#             node_stack.append(node)
        
#         if node.left:
#             node_stack.append(node.left)
        
#         if not (node.right or node.left):
#             break
        
#     while node_stack:
#         tmp = node_stack.pop()
#         res.append(tmp.val)
    
#     return res

def inorderTraversal(root):
    res = []
    node_stack = []
    cur = root
    
    while node_stack or cur:
        if cur:
            node_stack.append(cur)
            cur = cur.left
        else:
            cur = node_stack.pop()
            res.append(cur.val)
            cur = cur.right 
            
    return res
    
# # test case 1
# node4 = TreeNode(1)
# node3 = TreeNode(2)
# node2 = TreeNode(6)
# node1 = TreeNode(4, node3, node4)
# node0 = TreeNode(5, node1, node2)

# test case 2
node2 = TreeNode(3)
node1 = TreeNode(2, node2)
node0 = TreeNode(1, None, node1)

t = inorderTraversal(node0)

