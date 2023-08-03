# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 07:52:22 2023

@author: xuk11
二叉树 中序遍历
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(node, node_lst):
    if not node:
        return

    inorder(node.left, node_lst)
    node_lst.append(node.val)
    inorder(node.right, node_lst)


def inorderTraversal(root):
    node_lst = []
    inorder(root, node_lst)

    return node_lst
