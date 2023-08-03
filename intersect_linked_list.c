/* 链表相交
 * https://leetcode.cn/problems/intersection-of-two-linked-lists-lcci/submissions/
 */
#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB);
int getLinkedListLength(struct ListNode *head);

int main()
{
    // 创建链表
    struct ListNode node_5 = {5, NULL};
    struct ListNode node_4 = {4, &node_5};
    struct ListNode node_3 = {3, &node_4};
    struct ListNode node_2 = {2, &node_3};
    struct ListNode node_1 = {1, &node_2};

    // 查看链表长度
    int n = getLinkedListLength(&node_1);
    printf("%d\n", n);

    system("Pause");
    return 0;
}

int getLinkedListLength(struct ListNode *head)
{
    if(head == NULL) { //当输入空链表时，head->next 没有所指
        return 0;
    }
    struct ListNode *cur = malloc(sizeof(struct ListNode));
    cur->next = head->next;
    int len = 0;
    while(cur) {
        len++;
        cur = cur->next;
    }
    return len;
}

struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB)
{
    struct ListNode *curA = headA;
    struct ListNode *curB = headB;
    int lenA = getLinkedListLength(headA);
    int lenB = getLinkedListLength(headB);
    int move = lenA - lenB;

    if(move > 0) { // lenA > lenB
        while(move) {
            curA = curA->next;
            move--;
        }
    } else if(move < 0) { // lenA < lenB
        move = -move;
        while(move) {
            curB = curB->next;
            move--;
        }
    } else {
        ;
    }

    int flag = 1; // 是否找到相交节点的标志位
    while(curA && curB) {
        if(curA == curB) {
            flag = 0;
            break;
        }
        curA = curA->next;
        curB = curB->next;
    }

    if(flag) {
        return NULL;
    }
    return curA;
}
