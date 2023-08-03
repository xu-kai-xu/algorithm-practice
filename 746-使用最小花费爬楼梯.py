# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 22:07:14 2023

@author: xukkk
746-使用最小花费爬楼梯

动态规划五部曲

1. dp数组及下标的含义
dp[i] 是到达第i级台阶的最小花费

2. 递推公式
dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2], cost[i - 2])


3. dp数组初始化
dp[0] = 0
dp[1] = 0


4. 确定遍历顺序
从前往后

5. 举例推导dp数组

"""
cost1 = [10,15,20]
cost2 = [1,100,1,1,1,100,1,1,100,1]

def minCostClimbingStairs(cost):
    dp = [0] * (len(cost) + 1)
    
    for i in range(2, len(cost) + 1):
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

    return dp[i]


minCostClimbingStairs(cost2)