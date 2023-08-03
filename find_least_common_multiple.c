/* 求1-n的最小公倍数，用6,10,100测试*/
#include <stdio.h>
#include <stdlib.h>

unsigned long long gcd(unsigned long long m, unsigned  long long n)
{
    unsigned long long res = m % n;
    if (res == 0) {
        return n;
    } else {
        return gcd(n, res);
    }
}

unsigned long long lcm(unsigned long long m, unsigned long long n)
{
    return m * n / gcd(m, n); 
}

int main()
{
    unsigned long long a = 6;
    unsigned long long b = 10;
    unsigned long long c = 100;

    unsigned long long res = 1;
    for (unsigned long long i = 1; i <= c; i++) {
        printf("lcm of %llu and %llu is ", res, i);
        res = lcm(res, i);
        printf("%llu .\n", res);
    }

    printf("lcm of 1 to %llu is: %llu\n", c, res);
    system("Pause");
    return 0;
}
