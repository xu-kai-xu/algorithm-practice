# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 20:41:10 2023

@author: xukkk
455 分发饼干

贪心解法

1. 优先拿小号饼干给胃口小的孩子
2. 优先拿大号饼干给胃口大的孩子
"""

g = [1,2,3]
s = [1,1]

g = [1,2]
s = [1,2,3]

def findContentChildren(g, s):
    child_num = 0  # 记录满足的小孩数量
    g_new = g.copy()
    s_new = s.copy()
    g_new.sort()
    s_new.sort()
    
    for cookie in s_new:
        for eat in g_new:
            if cookie >= eat:
                # 能吃饱
                child_num += 1
                g_new.remove(eat)  # 下次就不考虑这个孩子了
                break
            
    return child_num


findContentChildren(g, s)

