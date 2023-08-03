/* */
#include <stdio.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

void postOrder(struct TreeNode *node, int *returnSize, int *ret)
{
    if (node == NULL) {
        return;
    }

    postOrder(node->left, returnSize, ret);
    postOrder(node->right, returnSize, ret);
    ret[(*returnSize)++] = node->val;
}

int *postOrderTraversal(struct TreeNode *root, int *returnSize)
{
    int *ret = (int *)malloc(sizeof(int) * 100);
    *returnSize = 0;
    postOrder(root, returnSize, ret);
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

    int *returnSize = (int *)malloc(sizeof(int) * 1);
    int *ret = NULL;

    ret = postOrderTraversal(node1, returnSize);

    for (int i = 0; i < 3; i++) {
        printf("node %d = %d\n", i + 1, ret[i]);
    }

    free(returnSize);
    free(node1);
    free(node2);
    free(node3);

    returnSize = NULL;
    node1 = NULL;
    node2 = NULL;
    node3 = NULL;

    system("Pause");
    return 0;
}
