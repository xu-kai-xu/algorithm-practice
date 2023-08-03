/* 看完了王争的算法之美相关课程，自己写的冒泡排序*/
#include <stdio.h>
#include <stdlib.h>

void bubbleSort(int a[], int n);

int main()
{
    int n = 10;
    int array[] = { 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 };

    bubbleSort(array, n);

    for (int i = 0; i < n; i++ ) {
        printf("%d\t%d\n", i, array[i]);
    }
    printf("\n");

    system("Pause");
    return 0;
}

void bubbleSort(int a[], int n) {
    if (n <= 1) {
        // 当只有一个元素或没有元素时，无需操作
        return;
    }
    for (int i = 0; i < n; i++) {
        int flag = 0;  // 排序是否发生的标志位，每一次向后走一位要重新置为0
        for(int j = 0; j < n - i - 1; j++) {
            if (a[j] > a[j+1]) {
                int tmp = a[j];
                a[j] = a[j+1];
                a[j+1] = tmp;
                flag = 1;  // 每有一次交换，将flag 置为 1
            }
        }
        if (!flag) {
            break;
        }
    }
}