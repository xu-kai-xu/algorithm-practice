/* 19 删除链表倒数第n个节点 
 * 这是力扣上的代码 和我的稍有不同*/
#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* removeNthFromEnd(struct ListNode* head, int n);

int main()
{

    system("Pause");
    return 0;
}

struct ListNode *removeNthFromEnd(struct ListNode *head, int n)
{
    struct ListNode *dummy = malloc(sizeof(struct ListNode));
    // 问题 什么时候用 malloc，什么时候直接赋值
    dummy->val = 0;
    dummy->next = head;

    struct ListNode *fast = head;
    struct ListNode *slow = dummy;

    while(n > 0) {
        fast = fast->next;
        n--;
    }

    while (fast != NULL) {
        fast = fast->next;
        slow = slow->next;
    }

    slow->next = slow->next->next;
    head = dummy->next;
    free(fast);
    free(dummy);
    return head;
}
