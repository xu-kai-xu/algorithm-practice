from removeNthFromEnd import ListNode, removeNthFromEnd, traverse_linked_list
import pytest

node_5 = ListNode(5)
node_4 = ListNode(4, node_5)
node_3 = ListNode(3, node_4)
node_2 = ListNode(2, node_3)
node_1 = ListNode(1, node_2)

def test_traverse():
    head_node = node_1
    expected = traverse_linked_list(head_node)
    assert expected == [1, 2, 3, 4, 5]

def test_onlyOneNode():
    head_node = node_5
    expected = removeNthFromEnd(head_node, 1)
    assert expected == None

# def test_blank_linked_list():
#     expected = removeNthFromEnd(None, 1)
#     assert expected == None

def test_case_one():
    head_node = node_1
    expected = removeNthFromEnd(head_node, 2)
    assert traverse_linked_list(expected) == [1, 2, 3, 5]