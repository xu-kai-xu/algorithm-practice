# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 08:09:32 2023

@author: xukkk

0 1 背包理论基础

1. dp数组和下标含义
    二维数组 dp[i][j] 表示从下标为 0 - i 的物品任取，
    放进容量为j的背包，价值总和最大是多少。

2 递推关系
dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i])


3. dp数组初始化
dp[0][:] 需要初始化
dp[:][0] 需要初始化
可以都初始化为0，方便一些，之后都会覆盖

4. 遍历顺序

5. 举例推导dp数组

weight = [1, 3, 4]
value = [15, 20, 30]

"""
weight = [1, 3, 4]
value = [15, 20, 30]

# 创建dp数组
# 3件物品，重量为4 dp[3][4]

dp = []
for _ in range(len(weight)):
    row = [0] * (weight[-1] + 1)
    dp.append(row[:])
    
# 初始化
for i in range(len(dp[0])):
    if i >= weight[0]:
        dp[0][i] = value[0]

# 递推
for j in range(1, len(dp[0])):
    for i in range(1, len(dp)):
        if j >= weight[i]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])
        else:
            dp[i][j] = dp[i - 1][j]
