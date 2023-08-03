# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 08:13:13 2023

@author: xuk11

插入排序的python版本
"""

test1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
test = test1

def insertition_sort(array):
    if len(array) <= 1:
        return array
    size = len(array)
    for i in range(1, size):
        for j in range(i - 1, -1, -1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

insertition_sort(test)
