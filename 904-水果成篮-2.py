# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 15:51:19 2022

@author: xuk11
"""
# 作者：lcbin
# 链接：https://leetcode.cn/problems/fruit-into-baskets/solution/by-lcbin-e1fw/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

from collections import Counter


def totalFruit(fruits):
    cnt = Counter()
    ans = j = 0
    for i, x in enumerate(fruits):
        cnt[x] += 1
        while len(cnt) > 2:
            y = fruits[j]
            cnt[y] -= 1
            if cnt[y] == 0:
                cnt.pop(y)
            j += 1
        ans = max(ans, i - j + 1)
    return ans

fruits = [3,3,3,1,2,1,1,2,3,3,4]
#fruits = [1, 2, 1]
#fruits = [0,1,2,2]
t = totalFruit(fruits)
print(t)