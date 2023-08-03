// 二叉树统一迭代法
// https://programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E7%BB%9F%E4%B8%80%E8%BF%AD%E4%BB%A3%E6%B3%95.html#%E8%BF%AD%E4%BB%A3%E6%B3%95%E4%B8%AD%E5%BA%8F%E9%81%8D%E5%8E%86
#include <stdio.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

int *preorderTraversal(struct TreeNode *root, int *returnSize)
{
    int *res = (int *)malloc(sizeof(int) * 100);
    struct TreeNode *node_stack[100] = {0};
    int top = -1;
    struct TreeNode *cur = NULL;
    *returnSize = 0;

    if (root != NULL) {
        node_stack[++top] = root; // 根节点入栈
    }

    while (top > -1) { // top == -1 说明 栈空
        cur = node_stack[top];  // 从栈顶取出当前节点，但并未弹出
        if (cur != NULL) {
            top--; // 弹出栈顶元素

            if (cur->right) {
                node_stack[++top] = cur->right;
            }

            if (cur->left) {
                node_stack[++top] = cur->left;
            }

            node_stack[++top] = cur;
            node_stack[++top] = NULL;
        } else {
            top--; // 弹出栈顶的空元素
            cur = node_stack[top--];
            res[(*returnSize)++] = cur->val;
        }
    }
    return res;
}

int *inorderTraversal(struct TreeNode *root, int *returnSize)
{
    int *res = (int *)malloc(sizeof(int) * 100);
    struct TreeNode *node_stack[100] = {0};
    int top = -1;
    struct TreeNode *cur = NULL;
    *returnSize = 0;

    if (root != NULL) {
        node_stack[++top] = root; // 根节点入栈
    }

    while (top > -1) { // top == -1 说明 栈空
        cur = node_stack[top];  // 从栈顶取出当前节点，但并未弹出
        if (cur != NULL) {
            top--; // 弹出栈顶元素

            if (cur->right) {
                node_stack[++top] = cur->right;
            }

            node_stack[++top] = cur;
            node_stack[++top] = NULL;

            if (cur->left) {
                node_stack[++top] = cur->left;
            }
        } else {
            top--; // 弹出栈顶的空元素
            cur = node_stack[top--];
            res[(*returnSize)++] = cur->val;
        }
    }
    return res;
}

int *postorderTraversal(struct TreeNode *root, int *returnSize)
{
    int *res = (int *)malloc(sizeof(int) * 100);
    struct TreeNode *node_stack[100] = {0};
    int top = -1;
    struct TreeNode *cur = NULL;
    *returnSize = 0;

    if (root != NULL) {
        node_stack[++top] = root; // 根节点入栈
    }

    while (top > -1) { // top == -1 说明 栈空
        cur = node_stack[top];  // 从栈顶取出当前节点，但并未弹出
        if (cur != NULL) {
            top--; // 弹出栈顶元素

            node_stack[++top] = cur;
            node_stack[++top] = NULL;

            if (cur->right) {
                node_stack[++top] = cur->right;
            }

            if (cur->left) {
                node_stack[++top] = cur->left;
            }
        } else {
            top--; // 弹出栈顶的空元素
            cur = node_stack[top--];
            res[(*returnSize)++] = cur->val;
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

    // res = preorderTraversal(node0, returnSize);
    res = inorderTraversal(node0, returnSize);
    // res = postorderTraversal(node0, returnSize);

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