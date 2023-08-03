#include <stdio.h>
#include <stdlib.h>

struct TreeNode
{
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

// 反转列表
void reverse_array(int *array, int n)
{
    int start = 0, end = n - 1;
    int tmp = 0;
    while (start < end) {
        tmp = array[start];
        array[start] = array[end];
        array[end] = tmp;

        start++;
        end--;
    }
}

int *postorderTraversal(struct TreeNode *root, int *returnSize)
{
    struct TreeNode *node_stack[100] = {0};
    int *res = (int *)malloc(sizeof(int) * 100);
    int node_ptr = -1;
    struct TreeNode *cur = NULL;
    *returnSize = 0;  // returnSize 一定要初始化

    node_stack[++node_ptr] = root;  // 根节点加入栈中
    while (node_ptr > -1) {
        cur = node_stack[node_ptr];

        if (cur) {
            res[(*returnSize)++] = cur->val;
            node_ptr--; // 将栈顶指针减一，即弹出
        } else {
            break;
        }

        if (cur->left) {
            node_stack[++node_ptr] = cur->left;
        }
        if (cur->right) {
            node_stack[++node_ptr] = cur->right;
        }
    }

    reverse_array(res, *returnSize);

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

    res = postorderTraversal(node0, returnSize);

    for (int i = 0; i < *returnSize; i++)
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