#include <stdio.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

int main() {
    // 初始化节点3
    struct TreeNode node3 = {3, NULL, NULL};

    // 初始化节点2，并将其左节点指向节点3
    struct TreeNode node2 = {2, &node3, NULL};

    // 初始化节点1，并将其右节点指向节点2
    struct TreeNode node1 = {1, NULL, &node2};

    // 输出节点1的值和右节点的值
    printf("node1: val=%d, right=%d\n", node1.val, node1.right->val);

    system("pause");
    return 0;
}
