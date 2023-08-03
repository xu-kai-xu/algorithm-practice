# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 07:50:38 2023

@author: xukkk
94 二叉树中序遍历 统一方法
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
def inorderTraversal(root):
    res = []
    node_stack = []
    
    if root:
        node_stack.append(root)
        
    while node_stack:
        node = node_stack[-1]
        if node:
            node_stack.pop()  # 根/父节点弹出，之后再入栈
            
            if node.right:
                node_stack.append(node.right)  # 右节点入栈
                
            node_stack.append(node)  # 父节点入栈
            node_stack.append(None)  # 标记已经访问过的节点
            
            if node.left:
                node_stack.append(node.left)  # 左节点入栈
        
        else:  #遇到空节点，才将空节点的下一个节点放入res中
            node_stack.pop()  # 弹出空节点
            node = node_stack.pop()  # 空节点前一个节点
            res.append(node.val)
            
    return res


def preorderTraversal(root):
    res = []
    node_stack = []
    
    if root:
        node_stack.append(root)
        
    while node_stack:
        node = node_stack[-1]
        if node:
            node_stack.pop()  # 根/父节点弹出，之后再入栈
            
            if node.right:
                node_stack.append(node.right)  # 右节点入栈
                
            if node.left:
                node_stack.append(node.left)  # 左节点入栈
                
            node_stack.append(node)  # 父节点入栈
            node_stack.append(None)  # 标记已经访问过的节点
            
        
        else:  #遇到空节点，才将空节点的下一个节点放入res中
            node_stack.pop()  # 弹出空节点
            node = node_stack.pop()  # 空节点前一个节点
            res.append(node.val)
            
    return res    


def postorderTraversal(root):
    res = []
    node_stack = []
    
    if root:
        node_stack.append(root)
        
    while node_stack:
        node = node_stack[-1]
        if node:
            node_stack.pop()  # 根/父节点弹出，之后再入栈
            
            node_stack.append(node)  # 父节点入栈
            node_stack.append(None)  # 标记已经访问过的节点
            
            if node.right:
                node_stack.append(node.right)  # 右节点入栈
                
            if node.left:
                node_stack.append(node.left)  # 左节点入栈
            
            
        
        else:  #遇到空节点，才将空节点的下一个节点放入res中
            node_stack.pop()  # 弹出空节点
            node = node_stack.pop()  # 空节点前一个节点
            res.append(node.val)
            
    return res
            
                
node4 = TreeNode(1)
node3 = TreeNode(2)
node2 = TreeNode(6)
node1 = TreeNode(4, node3, node4)
node0 = TreeNode(5, node1, node2)

t1 = inorderTraversal(node0)           
t2 = preorderTraversal(node0) 
t3 = postorderTraversal(node0) 
                
                
                
                
                
                
                
                
                
                
                
                
 
