class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
        dummy = ListNode(-1, head)  # dummy node
        fast = slow = dummy
        while (n + 1):
            fast = fast.next
            n -= 1

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next

def traverse_linked_list(head):
    test = head
    res = []
    while test:
        res.append(test.val)
        test = test.next
    return res