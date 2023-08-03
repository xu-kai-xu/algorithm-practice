// https://leetcode.cn/problems/remove-linked-list-elements/
// 代码摘抄自 代码随想录

#include <stdio.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* removeElements(struct ListNode* head, int val){
    typedef struct ListNode ListNode;
    ListNode *shead;
    shead = (ListNode*)malloc(sizeof(ListNode));
    shead->next = head;
    ListNode *cur = shead;
    while (cur->next != NULL) {
        if (cur->next->val == val) {
            ListNode *tmp = cur->next;
            cur->next = cur->next->next;
            free(tmp);
        }
        else {
            cur = cur->next;
        }
    }
    head = shead->next;
    free(shead);
    return head;
}

int main()
{

    system("Pause");
    return 0;
}