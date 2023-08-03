# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 10:43:25 2023

@author: xukkk

62-不同路径

动规五部曲

1. dp[i][j] 从 出发点到 i行j列的所有走法

2. 递推公式 可以从上面来，可以从左边来
    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

3. 初始化
    dp[0][0] = 1
    dp[0][1] = 1
    dp[1][0] = 1
    dp[1][1] = 2

第一行和第一列需要初始化为 1

4. 遍历顺序，从左到右一层一层遍历【目前还没有见过别的遍历顺序】

5. 举例推导：
"""

m1, n1 = 3, 7
m2, n2 = 3, 2

def uniquePaths(m, n):
    dp = []
    dp.append([1] * n)
    line = [1] + [0] * (n - 1)
    for _ in range(1, m):  # 构造dp数组
        dp.append(line[:])

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]



t = uniquePaths(m2, n2)


# 斐波那契数列
