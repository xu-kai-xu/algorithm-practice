/* 环形链表 */
#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode *detectCycle(struct ListNode *head);

int main()
{

    system("Pause");
    return 0;
}

struct ListNode *detectCycle(struct ListNode *head)
{
    struct ListNode *fast = head;
    struct ListNode *slow = head;
    struct ListNode *p = head;
    struct ListNode *q = head;

    while (fast && fast->next) {
        fast = fast->next->next;
        slow = slow->next;

        if (fast == slow) {
            q = slow;
            while (p != q) {
                p = p->next;
                q = q->next;
            }
            return p;
        }
    }
    return NULL;
}
