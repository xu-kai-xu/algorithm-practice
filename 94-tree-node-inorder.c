#include <stdio.h>
#include <stdlib.h>

struct TreeNode
{
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

void inOrder(struct TreeNode *node, int *returnSize, int *ret)
{
    if (node == NULL) {
        return;
    }

inOrder(node->left, returnSize, ret);
ret[(*returnSize)++] = node->val;
inOrder(node->right, returnSize, ret);

}

int *inorderTraversal(struct TreeNode *root, int *returnSize)
{
    int *ret = (int *)malloc(sizeof(int) * 100);
    *returnSize = 0;
    inOrder(root, returnSize, ret);

    return ret;
}

int main()
{
    // 初始化二叉树节点
    struct TreeNode *node3 = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    struct TreeNode *node2 = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    struct TreeNode *node1 = (struct TreeNode *)malloc(sizeof(struct TreeNode));

    node3->val = 3;
    node3->left = NULL;
    node3->right = NULL;

    node2->val = 2;
    node2->left = node3;
    node2->right = NULL;

    node1->val = 1;
    node1->left = NULL;
    node1->right = node2;

    int *ret = NULL;
    int *returnSize = (int *)malloc(sizeof(int));

    ret = inorderTraversal(node1, returnSize);

    for (int i = 0; i < 3; i++) {
        printf("node %d = %d\n", i + 1, ret[i]);
    }

    free(ret);
    free(returnSize);
    system("pause");
    return 0;
}