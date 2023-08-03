# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 19:36:04 2023

@author: xukkk

416 分割等和子集


nums数组和的一半可以当作是背包容量，
数组本身可以当作values


动规五部曲 采用滚动数组的方法

1. dp数组和下标的含义
dp[j]表示，重量为j时的价值总和。

2. 递推关系
dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

3. dp数组初始化
可以全部初始化为0

4. 遍历顺序
从后向前遍历
当dp[j] == sum 时结束

5. 举例推导dp数组

"""

nums1 = [1, 5, 11, 5]
nums2 = [1, 2, 3, 5]


# dp数组初始化
# half = sum(nums) // 2
# dp = [0] * (half + 1)

# for i in range(len(nums)):
#     for j in tuple(range(half + 1))[::-1]:
#         if j >= nums[i]:
#             dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
#             if dp[j] == half:
#                 print(True)

# print(False)

def canPartition(nums):
    if (sum(nums) % 2):
        return False
    
    half = sum(nums) // 2
    dp = [0] * (half + 1)
    
    for i in range(len(nums)):
        for j in tuple(range(half + 1))[::-1]:
            if j >= nums[i]:
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
                if dp[j] == half:
                    return True
    return False


canPartition(nums1)
