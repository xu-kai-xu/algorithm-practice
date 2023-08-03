/* 707 设计链表
 * 摘自代码随想录
 * https://programmercarl.com/0707.%E8%AE%BE%E8%AE%A1%E9%93%BE%E8%A1%A8.html#%E5%85%B6%E4%BB%96%E8%AF%AD%E8%A8%80%E7%89%88%E6%9C%AC */
#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

typedef struct MyLinkedList {
    int val;
    struct MyLinkedList *next;
} MyLinkedList;

MyLinkedList *myLinkedListCreate(void);
int myLinkedListGet(MyLinkedList *obj, int index);
void myLinkedListAddAtHead(MyLinkedList *obj, int val);
void myLinkedListAddAtTail(MyLinkedList *obj, int val);
void myLinkedListAddAtIndex(MyLinkedList *obj, int index, int val);
void myLinkedListDeleteAtIndex(MyLinkedList *obj, int index);
void myLinkedListFree(MyLinkedList *obj);


int main()
{
    MyLinkedList *obj = myLinkedListCreate();
    myLinkedListAddAtHead(obj, 2);
    myLinkedListDeleteAtIndex(obj, 1);
    myLinkedListAddAtHead(obj, 2);
    myLinkedListAddAtHead(obj, 7);
    myLinkedListAddAtHead(obj, 3);
    myLinkedListAddAtHead(obj, 2);
    myLinkedListAddAtHead(obj, 5);
    myLinkedListAddAtTail(obj, 5);
    int param_1 = myLinkedListGet(obj, 5);
    printf("\n%d\n", param_1);
    myLinkedListDeleteAtIndex(obj, 6);
    myLinkedListDeleteAtIndex(obj, 4);

    // myLinkedListAddAtIndex(obj, index, val);

    myLinkedListFree(obj);
    system("Pause");
    return 0;
}

MyLinkedList *myLinkedListCreate(void) {
    // 使用虚拟头节点
    MyLinkedList *dummy = (MyLinkedList*)malloc(sizeof(MyLinkedList));
    dummy->next = NULL;
    return dummy;
}

int myLinkedListGet(MyLinkedList *obj, int index) {
    MyLinkedList *cur = obj->next;  // obj->next 指向真实的第一个节点，虚拟头结点的下一位
    for (int i = 0; cur != NULL; i++) {
        if (i == index) {
            return cur->val;
        } else {
            cur = cur->next;
        }
    }
    return -1;
}

void myLinkedListAddAtHead(MyLinkedList *obj, int val) {
    MyLinkedList *nhead = (MyLinkedList*)malloc(sizeof(MyLinkedList));
    nhead->val = val;
    nhead->next = obj->next;
    obj->next = nhead;
}

void myLinkedListAddAtTail(MyLinkedList * obj, int val) {
    MyLinkedList *cur =obj;
    while(cur->next != NULL) {
        cur = cur->next;
    }
    MyLinkedList *ntail = (MyLinkedList*)malloc(sizeof(MyLinkedList));
    ntail->val = val;
    ntail->next = NULL;
    cur->next = ntail;
}

void myLinkedListAddAtIndex(MyLinkedList *obj, int index, int val) {
    if (index == 0) {
        myLinkedListAddAtHead(obj, val);
        return;
    }
    MyLinkedList *cur = obj->next;
    for (int i = 1; cur != NULL; i++) {
        if (i == index) {
            MyLinkedList *newnode = (MyLinkedList*)malloc(sizeof(MyLinkedList));
            newnode->val = val;
            newnode->next = cur->next;
            cur->next = newnode;
            return;
        } else {
            cur = cur->next;
        }
    }
}

void myLinkedListDeleteAtIndex(MyLinkedList *obj, int index) {
    if (index == 0) {
        MyLinkedList *tmp = obj->next;
        if (tmp != NULL) {
            obj->next = tmp->next;
            free(tmp);
        }
        return;
    }
    MyLinkedList *cur = obj->next;
    for(int i = 1; cur != NULL && cur->next != NULL; i++) {
        if (i == index) {
            MyLinkedList *tmp = cur->next;
            if (tmp != NULL) {
                cur->next = tmp->next;
                free(tmp);
            }
            return;
        } else {
            cur = cur->next;
        }
    }
}

void myLinkedListFree(MyLinkedList *obj) {
    while (obj != NULL) {
        MyLinkedList *tmp = obj;
        obj = obj->next;
        free(tmp);
    }
}


