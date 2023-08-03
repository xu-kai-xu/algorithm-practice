# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 21:55:32 2023

@author: xukkk

343 整数拆分
https://leetcode.cn/problems/integer-break/
把一个整数拆成2个或者更多整数的和，要求使拆分后整数的乘积最大化

动规五部曲：

1. dp[i]，拆分数字i可以得到的最大乘积

2. 递推公式：
dp[i] = max(j * (i - j), j * dp[i - j]), j [1, i)
取最大值的第一项是拆成两项，第二项是拆成多项

3. 初始化
dp[0] = 1  # 为方便
dp[1] = 1  # 为方便
dp[2] = 1
dp[3] = 2


dp[10] = 36


4. 遍历顺序，从1到i

5. 举例推导 
"""

n1 = 2
n2 = 10


def integerBreak(n):
    dp = [1] * (n + 1)
    
    for i in range(2, n + 1):
        for j in range(1, i):
            # tmp = max(j * (i - j), j * dp[i - j])  # 临时记录最大值
            # if tmp > dp[i]:
            #     dp[i] = tmp
            dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))
                
    return dp[n]


integerBreak(n2)


