# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 07:53:50 2023

@author: xukkk
102- 二叉树层序遍历
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

# 迭代法
# def levelOrder(root):
#     res = []
#     node_que = []
    
#     if root:    
#         node_que.append(root)
#     else:
#         return res

#     while node_que:
#         size = len(node_que)  # 确定当前层的节点数量
#         res_lev = []  # 放每层节点
#         while (size):
#             node = node_que.pop(0)
#             size -= 1
#             res_lev.append(node.val)
#             if node.left:
#                 node_que.append(node.left)
#             if node.right:
#                 node_que.append(node.right)
             
#         res.append(res_lev)
            
#     return res


# 递归法
def level_trans(node, res, depth):
    if node is None:
        return
    
    if len(res) == depth:
        res.append([])  # 添加新的空数组
    
    res[depth].append(node.val)
    level_trans(node.left, res, depth + 1)
    level_trans(node.right, res, depth + 1)

def levelOrder(root):
    res = []
    depth = 0
    level_trans(root, res, depth)
    return res

node1 = TreeNode(1)
node3 = TreeNode(3)
node5 = TreeNode(5)
node8 = TreeNode(8)
node4 = TreeNode(4, node1, node3)
node7 = TreeNode(7, node5, node8)
node6 = TreeNode(6, node4, node7)

t = levelOrder(node6)

