# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 17:11:29 2022

@author: xuk11
"""
raw = '4 2 K A'
nums = raw.split(' ')

def guess_24(nums):
    #todo 需要写4个数字的排列出来
    if ('joker' in nums) or ('JOKER' in nums):
        return 'ERROR'

    # 所有可能的数字排列
    nums_arrang = [[nums[0], nums[1], nums[2], nums[3]],
                   [nums[0], nums[1], nums[3], nums[2]],
                   [nums[0], nums[2], nums[1], nums[3]],
                   [nums[0], nums[2], nums[3], nums[1]],
                   [nums[0], nums[3], nums[2], nums[1]],
                   [nums[0], nums[3], nums[1], nums[2]],
                   [nums[1], nums[0], nums[2], nums[3]],
                   [nums[1], nums[0], nums[3], nums[2]],
                   [nums[1], nums[2], nums[0], nums[3]],
                   [nums[1], nums[2], nums[3], nums[0]],
                   [nums[1], nums[3], nums[2], nums[0]],
                   [nums[1], nums[3], nums[0], nums[2]],
                   [nums[2], nums[1], nums[0], nums[3]],
                   [nums[2], nums[1], nums[3], nums[0]],
                   [nums[2], nums[0], nums[1], nums[3]],
                   [nums[2], nums[0], nums[3], nums[1]],
                   [nums[2], nums[3], nums[0], nums[1]],
                   [nums[2], nums[3], nums[1], nums[0]],
                   [nums[3], nums[0], nums[1], nums[2]],
                   [nums[3], nums[0], nums[2], nums[1]],
                   [nums[3], nums[1], nums[2], nums[0]],
                   [nums[3], nums[1], nums[0], nums[2]],
                   [nums[3], nums[2], nums[1], nums[0]],
                   [nums[3], nums[2], nums[0], nums[1]]]


    operands_perm = [['+', '-', '*'], ['+', '-', '/'],
                       ['-', '*', '/'], ['+', '*', '/']]

    # 所有可能的运算符排列
    operands_arrang = []
    for perm in operands_perm:
        one = [[perm[i], perm[j], perm[k]] for i in range(3) for j in range(3) for k in range(3)]
        operands_arrang.append(one)


    return operands_arrang


guess_24(nums)


operands_perm = [['+', '-', '*'], ['+', '-', '/'],
                   ['-', '*', '/'], ['+', '*', '/']]

mm = [[perm[i], perm[j], perm[k]] for perm in operands_perm  for i in range(3) for j in range(3) for k in range(3)]
