/* 19 删除链表倒数第n个节点 */
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
    struct ListNode *fast = malloc(sizeof(struct ListNode));
    struct ListNode *slow = malloc(sizeof(struct ListNode));
    dummy->next = head;
    fast = slow = dummy;

    while(n + 1 > 0) {
        fast = fast->next;
        n--;
    }

    while (fast != NULL) {
        fast = fast->next;
        slow = slow->next;
    }

    slow->next = slow->next->next;
    // free(slow); 这个不能释放
    free(fast);
    // free(dummy); 这个释放后也会报错，用例通不过
    return dummy->next;
}
