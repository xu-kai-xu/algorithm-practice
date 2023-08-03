#include <stdio.h>
#include <stdlib.h>

struct TreeNode
{
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

int *inorderTraversal(struct TreeNode *root, int *returnSize)
{
    struct TreeNode *cur = root;  // 节点指针,首先指向根节点
    struct TreeNode *node_stack[100] = {0};
    int stack_ptr = -1;
    *returnSize = 0;
    int *res = (int *)malloc(sizeof(int) * 100);

    while ((cur != NULL) || stack_ptr > -1) {
        if (cur != NULL) {
            node_stack[++stack_ptr] = cur;
            cur = cur->left;
        } else {
            cur = node_stack[stack_ptr--];
            res[(*returnSize)++] = cur->val;
            cur = cur->right;
        }
    }

    return res;
}

int main()
{
    // 初始化二叉树
    struct TreeNode *node4 = (struct TreeNode *)malloc(sizeof(struct TreeNode) * 1);
    struct TreeNode *node3 = (struct TreeNode *)malloc(sizeof(struct TreeNode) * 1);
    struct TreeNode *node2 = (struct TreeNode *)malloc(sizeof(struct TreeNode) * 1);
    struct TreeNode *node1 = (struct TreeNode *)malloc(sizeof(struct TreeNode) * 1);
    struct TreeNode *node0 = (struct TreeNode *)malloc(sizeof(struct TreeNode) * 1);

    node3->val = 2;
    node3->left = NULL;
    node3->right = NULL;

    node2->val = 6;
    node2->left = NULL;
    node2->right = NULL;

    node4->val = 1;
    node4->left = NULL;
    node4->right = NULL;

    node1->val = 4;
    node1->left = node3;
    node1->right = node4;

    node0->val = 5;
    node0->left = node1;
    node0->right = node2;

    int *res = NULL;
    int *returnSize = (int *)malloc(sizeof(int));

    res = inorderTraversal(node0, returnSize);

    for (int i = 0; i < 10; i++)
    {
        printf("%d\t", res[i]);
    }
    printf("\n");

    free(node4);
    node4 = NULL;
    free(node3);
    node3 = NULL;
    free(node2);
    node2 = NULL;
    free(node1);
    node1 = NULL;
    free(node0);
    node0 = NULL;

    free(res);
    res = NULL;

    free(returnSize);
    returnSize = NULL;

    system("pause");
    return (0);
}