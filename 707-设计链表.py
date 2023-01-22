"""
707 设计链表

test example 1
["MyLinkedList","addAtHead","deleteAtIndex","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtTail","get","deleteAtIndex","deleteAtIndex"]
[[],[2],[1],[2],[7],[3],[2],[5],[5],[5],[6],[4]]

test example 2
["MyLinkedList","addAtHead","get","addAtHead","addAtHead","deleteAtIndex","addAtHead","get","get","get","addAtHead","deleteAtIndex"]
[[],[4],[1],[1],[5],[3],[7],[3],[3],[3],[1],[4]]

test example 3
["MyLinkedList","addAtHead","addAtIndex","get"]
[[],[2],[0,1],[1]]

test example 4
["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get","get","deleteAtIndex","deleteAtIndex","get","deleteAtIndex","get"]
[[],[1],[3],[1,2],[1],[1],[1],[3],[3],[0],[0],[0],[0]]

test example 5
["MyLinkedList","addAtIndex","get"]
[[],[1,0],[0]]
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        # 初始化设置一个虚拟节点
        self.dummy = ListNode(val = -1, next=None)

    def get(self, index: int) -> int:
        ret = self.dummy
        if not ret.next:
            return -1  # 空节点
        while index >= 0:
            ret = ret.next
            index -= 1
            if not ret.next:
                break
        if index == -1:
            return ret.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val=val, next=None)
        newNode.next = self.dummy.next
        self.dummy.next = newNode

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val=val, next=None)
        ret = self.dummy
        while ret.next:
            ret = ret.next
        # 循环执行完毕后，走到尾节点
        ret.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= 0:
            return self.addAtHead(val=val)
        newNode = ListNode(val=val, next=None)
        ret = self.dummy
        if (not ret.next) and (index > 0):  # 空节点时，如果index大于0，不插入
            return None
        while index >= 1:
            ret = ret.next
            index -= 1
            if not ret.next:
                break
        # 循环之后，此时ret到了第 index-1 个节点的位置
        if index == 0:
            newNode.next = ret.next
            ret.next = newNode
        else:
            pass  # index 大于链表长度，不插入节点

    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            pass
        ret = self.dummy
        while index >= 1:
            ret = ret.next
            index -= 1
            if not ret.next:
                break
        if index == 0 and (not ret.next):
            ret = None
        elif index == 0 and (ret.next.next):
            ret.next = ret.next.next
        elif index == 0 and (not ret.next.next):
            ret.next = None
        else:
            pass


def test1():
    print('running test1~')
    obj = MyLinkedList()
    obj.addAtHead(2)
    obj.deleteAtIndex(1)
    obj.addAtHead(2)
    obj.addAtHead(7)
    obj.addAtHead(3)
    obj.addAtHead(2)
    obj.addAtHead(5)
    obj.addAtTail(5)
    obj.get(5)
    obj.deleteAtIndex(6)
    obj.deleteAtIndex(4)

def test2():
    print('running test2~')
    obj = MyLinkedList()
    obj.addAtHead(4)
    obj.get(1)
    obj.addAtHead(1)
    obj.addAtHead(5)
    obj.deleteAtIndex(3)
    obj.addAtHead(7)
    obj.get(3)
    obj.get(3)
    obj.get(3)
    obj.addAtHead(1)
    obj.deleteAtIndex(4)

def test3():
    print('running test3~')
    obj = MyLinkedList()
    obj.addAtHead(2)
    # print(obj.get(0))
    obj.addAtIndex(0, 1)
    # print(obj.get(0))
    obj.get(1)
    # print(obj.get(0))
    # print(obj.get(1))

def test4():
    print('running test4~')
    obj = MyLinkedList()
    obj.addAtHead(1)
    obj.addAtTail(3)
    obj.addAtIndex(1, 2)
    obj.get(1)
    obj.deleteAtIndex(1)
    obj.get(1)
    obj.get(3)
    obj.deleteAtIndex(3)
    obj.deleteAtIndex(0)
    obj.get(0)
    obj.deleteAtIndex(0)
    obj.get(0)

def test5():
    print('running test5~')
    obj = MyLinkedList()
    obj.addAtIndex(1, 0)
    obj.get(0)


if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    # test4()
    test5()





