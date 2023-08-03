# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 22:30:31 2023

@author: xukkk

700 二叉搜索树
"""

from tree_node import TreeNode


def inOrderTraverse(node, val, res):
    if not node:
        return
    
    inOrderTraverse(node.left, val, res)

    if node.val == val:
        res.append(node.val)
    
    inOrderTraverse(node.right, val, res)
    
    
def preOrderTraverse(node, lst):
    if not node:
        return
    
    lst.append(node.val)
    preOrderTraverse(node.left, lst)
    preOrderTraverse(node.right, lst)
    
  
    


def searchBST(root, val):
    node_lst = []
    res = []
    inOrderTraverse(root, val, node_lst)
    if not node_lst:
        return None
    
    preOrderTraverse(node_lst[0], res)
    return res


# 代码随想录的解法

def searchBST(root, val):
    if root == None or root.val == val:
        return root
    res = None
    if (root.val > val):
        res = searchBST(root.left, val)
    if (root.val < val):
        res = searchBST(root.right, val)
    return res


node1 = TreeNode(val=1)
node3 = TreeNode(val=3)
node2 = TreeNode(val=2, left=node1, right=node3)
node7 = TreeNode(val=7)
node4 = TreeNode(val=4, left=node2, right=node7)


t = searchBST(node4, 5)


