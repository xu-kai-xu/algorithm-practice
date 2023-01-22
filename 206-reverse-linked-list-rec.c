/* 翻转链表 双指针*/
#include <stdio.h>
#include <stdlib.h>

typedef struct ListNode {
    int val;
    struct ListNode *next;
} ListNode;

ListNode *reverse(ListNode *pre, ListNode *cur);
ListNode *reverseList(ListNode *head);

int main()
{
    // 创建链表
    ListNode node_5 = {5, NULL};
    ListNode node_4 = {4, &node_5};
    ListNode node_3 = {3, &node_4};
    ListNode node_2 = {2, &node_3};
    ListNode node_1 = {1, &node_2};

    // linked list node traverse
    ListNode *node_ptr = &node_1; // 指向头结点的指针
    while(node_ptr != NULL) {
        printf("%d\n", node_ptr->val);
        node_ptr = node_ptr->next;
    }

    ListNode *new_node = reverseList(&node_1);

    printf("\n");

    ListNode *node_ptr_2 = new_node; // 指向头结点的指针
    while(node_ptr_2 != NULL) {
        printf("%d\n", node_ptr_2->val);
        node_ptr_2 = node_ptr_2->next;
    }

    system("Pause");
    return 0;
}

ListNode *reverse(ListNode *pre, ListNode *cur)
{
    if (cur == NULL) {
        return pre;
    }
    ListNode *temp = cur->next;
    cur->next = pre;
    return reverse(cur, temp);
}

ListNode *reverseList(ListNode *head)
{
    return reverse(NULL, head);
}
