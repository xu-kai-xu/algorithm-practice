# 206 翻转链表
# https://leetcode.cn/problems/reverse-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# def reverseList(head):
#     if not head:
#         return head
#     elif not head.next:
#         return head
#     else:
#         cur = head.next
#     pre = ListNode(head.val, next=None)  # 一个空节点

#     while cur.next:

#         tmp = cur.next
#         cur.next = pre
#         pre = cur
#         cur = tmp

#     # 循环过后，到达了最后一个节点
#     cur.next = pre
#     pre = cur

#     return pre

# 力扣上的例子
def reverseList(head):
    cur = head
    pre = None
    while cur:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
    return pre

# 反转链表的递归方法 1
def reverse(pre, cur):
    """
    input type: list node
    """
    if not cur:
        return pre
    temp = cur.next
    cur.next = pre
    return reverse(cur, temp)

def reverseList_rec(head):
    return reverse(None, head)

#---------------------------------
# test
def traverse_linked_list(head):
    test = head
    while test:
        print(test.val)
        test = test.next

node_5 = ListNode(5)
node_4 = ListNode(4, node_5)
node_3 = ListNode(3, node_4)
node_2 = ListNode(2, node_3)
node_1 = ListNode(1, node_2)

only_one_node = ListNode(10)

traverse_linked_list(node_1)

newhead = reverseList(node_1)

traverse_linked_list(newhead)
