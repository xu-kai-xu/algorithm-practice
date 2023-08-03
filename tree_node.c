#include <stdio.h>
#include <stdlib.h>

// typedef struct {
//     int val;
//     TreeNode *left;
//     TreeNode *right;
// } TreeNode;

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

void preOrder(struct TreeNode *node, int *ret, int returnSize)
{
    static int size = 0;
    // printf("size =  %d\n", size);
    if (node == NULL) {
        return;
    }
    // printf("node val = %d\n", node->val);
    ret[size++] = node->val;
    preOrder(node->left, ret, returnSize);
    preOrder(node->right, ret, returnSize);
}

void preorderTraversal(struct TreeNode *root, int returnSize, int *ret)
{
    preOrder(root, ret, returnSize);
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

    int returnSize = 3;
    int ret[3] = {0};

    preorderTraversal(node1, returnSize, ret);

    for (int i = 0; i < returnSize; i++) {
        printf("node %d = %d\n", i + 1, ret[i]);
    }

    // printf("node1 val = %d, left = %d, right = %d\n", node1->val, node1->left, node1->right->val);
    // printf("node1 val = %d, left = %d, right = %d\n", node2->val, node2->left->val, node2->right);
    // printf("node1 val = %d, left = %d, right = %d\n", node3->val, node3->left, node3->right);

    free(node3);
    node3 = NULL;
    free(node2);
    node2 = NULL;
    free(node1);
    node1 = NULL;
    system("pause");
    return 0;
}