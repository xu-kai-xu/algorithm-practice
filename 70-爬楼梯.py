# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 21:14:45 2023

@author: xukkk
70-爬楼梯
"""

def climbStairs(n):
    # dp[n] 爬第n级台阶有几种方法
    # dp[n] = dp[n - 1] + dp[n - 2]
    
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    dp_1 = 1
    dp_2 = 2
    dp_i = 0
    
    for i in range(3, n + 1):
        dp_i = dp_2 + dp_1
        dp_2, dp_1 = dp_i, dp_2
        
    return dp_i


climbStairs(5)

    
    

