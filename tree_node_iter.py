# 二叉树节点定义
# https://programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html#%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%AE%9A%E4%B9%89

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = None
        self.right = None

# 前序遍历
def preOrder(node: TreeNode, node_lst: list[TreeNode]) -> None:
    if not node:
        return

    node_lst.append(node.val)
    preOrder(node.left)
    preOrder(node.right)


def preorderTraversal(root: TreeNode) -> list[int]:
    node_lst = []
    preOrder(root, node_lst)

    return node_lst


# 后序遍历
def postOrder(node: TreeNode, node_lst: list[int]) -> int:
    if node == None:
        return

    postOrder(node.left)
    postOrder(node.right)
    node_lst.append(node.value)


def postorderTraversal(root: TreeNode) -> list[int]:
    node_lst = []
    postOrder(root, node_lst)

    return node_lst
