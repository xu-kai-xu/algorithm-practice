/* */
#include <stdio.h>
#include <stdlib.h>

int removeElement(int *nums, int numsSize, int val)
{
    int s = 0;
    for (int f = 0; f < numsSize; f++) {
        if (nums[f] != val) {
            nums[s] = nums[f];
            s++;
        }
    }
    return s;
}

int main()
{
    int nums1[] = {3, 2, 2, 3};
    int val1 = 3;
    int nums2[] = {0, 1, 2, 2, 3, 0, 4, 2};
    int val2 = 2;
    int s1 = removeElement(nums1, 4, 3);
    int s2 = removeElement(nums2, 8, 2);
    printf("s1 = %d\n", s1);
    printf("s2 = %d\n", s2);
    system("Pause");
    return 0;
}
