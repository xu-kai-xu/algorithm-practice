# 前序遍历 迭代法

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_trans(root):
    res = []
    node_stack = []

    node_stack.append(root)

    while node_stack:
        node = node_stack[-1]
        if node:
            res.append(node.val)
            node_stack.pop()
        else:
            break
        
        if node.right:
            node_stack.append(node.right)
        if node.left:
            node_stack.append(node.left)
        

    return res


node4 = TreeNode(1)
node3 = TreeNode(2)
node2 = TreeNode(6)
node1 = TreeNode(4, node3, node4)
node0 = TreeNode(5, node1, node2)

t = preorder_trans(node0)


