# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 17:00:33 2022

@author: xuk11
"""
n = 4
res = []

for i in range(n):
    res.append([0 for i in range(n)])


startx = starty = 0  # 定义每循环一个圈的起始位置
loop = n // 2  # 循环次数，即几圈
mid = n // 2  # 矩阵中间位置
count = 1  # 用来给矩阵中每一个位置赋值
offset = 1  # 控制每一条边遍历时的长度，每次循环右边界收缩一位


i, j = startx, starty
# x 和 y 分别对应二维数组的第一和第二索引


# 四个for循环模拟转了一圈
# 模拟填充上行从左到右（左闭右开）
for j in range(starty, n-offset):
    print(j)

    res[startx].append(count)
    count += 1
print(j)


n = 5
offset = 2

for j in range(n-offset, offset-1, -1):
    print(j)
    res[i][j] = count
    count += 1
j -= 1
