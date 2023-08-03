/**
 * 349 两个数组的交集
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdio.h>
#include <stdlib.h>

int *intersection(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize){
    int hash_table[1000] = { 0 };
    int lessSize = nums1Size < nums2Size ? nums1Size : nums2Size;
    int *result = (int*)malloc(lessSize * sizeof(int));
    int resultIndex = 0;
    int *tempNums;

    for (int i = 0; i < nums1Size; i++) {
        hash_table[nums1[i]]++;
    }
    for (int j = 0; j < nums2Size; j++) {
        if (hash_table[nums2[j]] > 0) {
            result[resultIndex] = nums2[j];
            resultIndex++;
            hash_table[nums2[j]] = 0;
        }
    }
    *returnSize = resultIndex;
    return result;
}

int main()
{
    int nums1[] = { 1, 2, 2, 1 };
    int nums2[] = { 2, 2};
    int nums3[] = { 4, 9, 5 };
    int nums4[] = { 9, 4, 9, 8, 4 };
    int nums1Size = 4;
    int nums2Size = 2;
    int nums3Size = 3;
    int nums4Size = 5;
    int *retSize = 0;

    int *ret = intersection(nums4, nums4Size, nums3, nums3Size, retSize);
    for (int i = 0; i < retSize; i++) {
        printf("%d\n", ret[i]);
    }

    system("Pause");
    return 0;
}
