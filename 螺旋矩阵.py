# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 22:56:21 2023

@author: xuk11
螺旋矩阵

1 对应的坐标是 0，0
"""
def location_level(x, y):
    level = 0
    if x < 0 and y < 0:
        if x < (y + 1):
            level = -x
        else:
            level = -y
    elif x < 0 and y > 0:
        if abs(x) < abs(y):
            level = abs(y)
        else:
            level = abs(x)
    elif x > 0 and y < 0:
        if abs(x) < abs(y):
            level = abs(y) - 1
        else:
            level = abs(x) - 1
    elif x > 0 and y > 0:
        if x - 1 > y:
            level = x
        else:
            level = y
    elif x < 0 and y == 0:
        level = -x
    elif x > 0 and y == 0:
        level = x - 1
    elif x == 0 and y > 0:
        level = y
    elif x == 0 and y < 0:
        level = -(y + 1)

    return level


def level_frame(level):
    accu = 0
    edge_len = 2 * level + 1  # 最外层边长-1
    for i in range(level + 1):
        accu += 8 * i + 4

    start_loc_x = 0
    start_loc_y = -1
    for j in range(1, level + 1):
        start_loc_x -= 1
        start_loc_y -= 1

    edge_value = []
    edge_loc = []

    for i in range(4):
        edge_value.append(accu - edge_len * i)

    edge_loc.append((start_loc_x, start_loc_y))
    edge_loc.append((start_loc_x + edge_len, start_loc_y))
    edge_loc.append((start_loc_x + edge_len, start_loc_y + edge_len))
    edge_loc.append((start_loc_x, start_loc_y + edge_len))

    return (edge_value, edge_loc)

# location_level(4, 5)
t = level_frame(3)


def spiral_matrix_gene(x, y):
    # 1的坐标为 0, 0。x y为相对于1的横纵坐标。
    if x == 0 and y == 0:
        return 1

    level = location_level(x, y)
    edge_val, edge_loc = level_frame(level)

    if y == edge_loc[0][1]:  # 下
        res = edge_val[0] - (x - edge_loc[0][0])
    elif x == edge_loc[1][0]:  # 右
        res = edge_val[1] - (y - edge_loc[1][1])
    elif y == edge_loc[2][1]:  # 上
        res = edge_val[2] - (edge_loc[2][0] - x)
    elif x == edge_loc[3][0]:  # 左
        res = edge_val[3] - (edge_loc[3][1] - y)
    else:
        print("unexpected situation.")

    return res


spiral_matrix_gene(-1, 1)
