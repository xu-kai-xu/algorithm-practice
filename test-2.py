# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 20:39:35 2022

@author: xuk11
"""
test1 = [[1, 1, 0],
         [1, 1, 0],
         [0, 0, 1]]
out1 = 2

test2 = [[1, 1, 0],
         [1, 1, 1],
         [0, 1, 1]]

out2 = 1

test3 = [[1,1,0,0],
         [1,1,0,0],
         [0,0,1,1],
         [0,0,1,1]]

test = test3



servers = {0: [], 1: [], 2: [], 3: []}

for i in range(4):
    for j in range(4):
        if test[i][j] == 1:
            servers[i] .append(j)

res = {}

for i in range(4):
    tmp = set(servers[i])
    for j in range(4):
        if (tmp.intersection(set(servers[j]))):
            tmp = tmp.union(set(servers[j]))

    res[i] = tmp


















