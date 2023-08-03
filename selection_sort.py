# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 22:27:41 2023

@author: xuk11
选择排序
"""

test = [5, 4, 3, 2, 1]
print(test)

def selection_sort(array):
    size = len(array)
    if (size <= 1):
        return
    for i in range(size):
        min_idx = i
        for j in range(i, size):
            if array[j] < array[min_idx]:
                min_idx = j

        array[i], array[min_idx] = array[min_idx], array[i]
    return

selection_sort(test)
print(test)
