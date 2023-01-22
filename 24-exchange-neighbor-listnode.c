/* 24 两两较远链表中的节点 双指针*/
#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode *swapPairs(struct ListNode *head);

int main()
{
    // 创建链表
    struct ListNode node_5 = {5, NULL};
    struct ListNode node_4 = {4, &node_5};
    struct ListNode node_3 = {3, &node_4};
    struct ListNode node_2 = {2, &node_3};
    struct ListNode node_1 = {1, &node_2};

    // linked list node traverse
    struct ListNode *node_ptr = &node_1; // 指向头结点的指针
    while(node_ptr != NULL) {
        printf("%d\n", node_ptr->val);
        node_ptr = node_ptr->next;
    }

    struct ListNode *new_node = swapPairs(&node_2);

    printf("\n");

    struct ListNode *node_ptr_2 = new_node; // 指向头结点的指针
    while(node_ptr_2 != NULL) {
        printf("%d\n", node_ptr_2->val);
        node_ptr_2 = node_ptr_2->next;
    }

    system("Pause");
    return 0;
}

struct ListNode *swapPairs(struct ListNode *head){
    struct ListNode *dummy = malloc(sizeof(struct ListNode));  // 动态分配内存
    dummy->next = head; // 虚拟头节点
    struct ListNode *cur = dummy;

    while ((cur->next != NULL) && (cur->next->next != NULL)) {
        // 删除节点
        struct ListNode *tempNode = cur->next;
        cur->next = cur->next->next;
        cur = cur->next;

        // 添加节点
        tempNode->next = cur->next;
        cur->next = tempNode;
        cur = cur->next;
    }
    return dummy->next;
}