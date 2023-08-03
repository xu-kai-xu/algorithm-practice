# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 20:22:13 2023

@author: xukkk
"""

stones1 = [2, 7, 4, 1, 8, 1]
stones2 = [31, 26, 33, 21, 40]


def lastStoneWeightII(stones):
    stones.sort()  # inplace 排序
    
    while len(stones) > 1:
        rck1 = stones.pop()
        rck2 = stones.pop()
        new_stone = abs(rck1 - rck2)
        if new_stone:
            stones.append(new_stone)
            stones.sort()
            
        print(stones)
    
    if len(stones) == 1:
        return stones[0]
    return 0


lastStoneWeightII(stones2)


"""
用 动规 的思路

把石头分成尽可能相等的两堆，这样相撞之后剩下的会最少
【真不知道这个思路时怎么想出来的】

1. dp数组和下标的含义
dp[j] 容量为j的背包中的最大重量

2. 递推关系
dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])

3. dp数组初始化
全零

4. 遍历顺序

5. 举例推导dp数组


"""
stones1 = [2, 7, 4, 1, 8, 1]
stones2 = [31, 26, 33, 21, 40]

half = sum(stones2) // 2
dp = [0] * (half + 1)

for i in range(len(stones2)):
    for j in tuple(range(len(dp)))[::-1]:
        if j >= stones2[i]:
            dp[j] = max(dp[j], dp[j - stones2[i]] + stones2[i])
            
print(sum(stones2) - dp[-1] * 2)

def lastStoneWeightII(stones):
    half = sum(stones) // 2
    dp = [0] * (half + 1)
    
    for i in range(len(stones)):
        for j in tuple(range(len(dp)))[::-1]:
            if j >= stones[i]:
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])      
                
    return sum(stones) - dp[-1] * 2


lastStoneWeightII(stones2)

# 暴力求 随机过程
from matplotlib import pyplot
from random import sample

stones2 = [31, 26, 33, 21, 40]

def crash_stone_simu(stones):
    stone_cp = stones[:]
    
    while len(stone_cp) > 1:
        choose = sample(stone_cp, 2)  # 取出2块石头
        stone_cp.remove(choose[0])
        stone_cp.remove(choose[1])
        stone_cp.append(abs(choose[0] - choose[1]))
    if len(stone_cp):
        return stone_cp[0]
    return 0


samples = []
    
for i in range(1000):
    samples.append(crash_stone_simu(stones2)) 
    
    
keys = set(samples)
stone_dict = {}
for key in keys:
    stone_dict.setdefault(key, 0)
for item in samples:
    stone_dict[item] += 1
    

pyplot.bar(stone_dict.keys(), stone_dict.values())
pyplot.show()
