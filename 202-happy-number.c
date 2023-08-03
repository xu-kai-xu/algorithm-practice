/* 202 快乐数 */
#include <stdio.h>
#include <stdlib.h>

int isHappy(int n);
int squareSum(int n);

int main()
{
    printf("%d\n", isHappy(2));
    system("Pause");
    return 0;
}

int isHappy(int n)
{
    int hash_table[1000] = { 0 };
    int sqSum = 0;
    while (1) {
        sqSum = squareSum(n);
        if (sqSum == 1) {
        return 1;
        } else if (hash_table[sqSum] == 1) {
            return 0;
        } else if (hash_table[sqSum] == 0) {
            hash_table[sqSum] = 1;
            n = sqSum;
        } 
    }
    
}

int squareSum(int n)
{
    int sum = 0;
    while (n / 10) {
        sum += (n % 10) * (n % 10);
        n = n / 10;
    }
    sum += (n % 10) * (n % 10);  // n / 10 == 0 说明只剩了个位数
    return sum;
}
