# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 16:14:40 2022

@author: xuk11
"""

n = 3
#n = 4

#res = [[1,2,3],[8,9,4],[7,6,5]]


def generateMatrix(n):
    res = []

    for i in range(n):
        res.append([0 for i in range(n)])

    startx = starty = 0  # 定义每循环一个圈的起始位置
    loop = n // 2  # 循环次数，即几圈
    mid = n // 2  # 矩阵中间位置
    count = 1  # 用来给矩阵中每一个位置赋值
    offset = 1  # 控制每一条边遍历时的长度，每次循环右边界收缩一位

    while loop:
        i, j = startx, starty
        # x 和 y 分别对应二维数组的第一和第二索引


        # 四个for循环模拟转了一圈
        # 模拟填充上行从左到右（左闭右开）
        for j in range(starty, n-offset):
            res[startx][j] = count
            count += 1
        j += 1  #  移动坐标到第n列

        # 模拟填充右行从上到下（左闭右开）
        for i in range(startx, n-offset):
            res[i][j] = count
            count += 1
        i += 1

        # 模拟填充下行从右到左(右闭左开)
        for j in range(n-offset, offset-1, -1):
            res[i][j] = count
            count += 1
        j -= 1

        # 模拟填充左列从下到上（下闭上开）
        for i in range(n-offset, offset-1, -1):
            res[i][j] = count
            count += 1
        i -= 1  # 一圈结束后，i，j返回这一圈的起始位置

        # 第二圈开始的时候，起始位置各加一
        startx += 1
        starty += 1

        # 每转一圈，每一条边遍历的长度减一，
        # 每一条边遍历长度为 n - offset
        offset += 1

        # 每循环一次，loop 减一
        loop -= 1

    # 这样如果是奇数行，最后正中央会剩下一个元素，
    if (n % 2) :
        res[mid][mid] = count

    return res


def print_matrix(m):
    for i in m:
        print(i)


print_matrix(generateMatrix(5))
