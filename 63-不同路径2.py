# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 11:10:28 2023

@author: xukkk
63-不同路径

有了障碍物，所以计算dp数组的时候，
1)先看一下dp[i][j]是不是障碍物
如果是，就跳过，如果不是，才算【可以给赋值为0】

2)再看一下上和左两个方向是不是障碍物，如果是，就不算，如果不是，就算。


如果给障碍物对应的dp数组赋值为0，似乎就不需要更改结构了。


3）还需要考虑到初始化时，第一行和第一列如果有障碍的情况，
  所以初始化分两步
1. 初始化为全0，
2. 第一行第一列没有障碍的地方初始化为1，有障碍的地方不变，仍然是0

"""



obstacleGrid_1 = [[0,0,0],[0,1,0],[0,0,0]]
obstacleGrid_2 = [[0,1],[0,0]]
obstacleGrid_3 = [[1,0]]
obstacleGrid_4 = [[0,0],[1,1],[0,0]]
obstacleGrid_5 = [[1],[0]]

def uniquePathsWithObstacles(obstacleGrid):
    # if obstacleGrid[0][0] == 1:
    #     return 0  # 当起始位置有障碍，就根本没法开始走了
    
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    
    dp = []
    line = [0] * n
    for _ in range(m):  # 构造dp数组
        dp.append(line[:])
        
    for i in range(len(dp[0])):
        if obstacleGrid[0][i] != 1:
            dp[0][i] = 1
        else:
            break  # 遇到第一行和第一列有障碍的位置，就在这个位置停止初始化
            
    for j in range(len(dp)):
        if obstacleGrid[j][0] != 1:
            dp[j][0] = 1
        else:
            break
    
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
    return dp[m - 1][n - 1]

        

t = uniquePathsWithObstacles(obstacleGrid_5)

