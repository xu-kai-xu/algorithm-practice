# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 16:11:53 2022

@author: xuk11
hj77 火车进站
https://www.nowcoder.com/practice/97ba57c35e9f4749826dc3befaeae109?tpId=37&tqId=21300&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D2%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=
"""

#n = 3
#nums = [1, 2, 3]

res = []  # 全局变量

"""
wait 表示
stack 栈中的元素
out

"""

def dfs(wait, stack, out):
    if (not wait) and (not stack):
        res.append(' '.join(map(str, out)))
    if wait:  # 入栈，一开始一股脑都入栈
        dfs(wait[1:], stack + [wait[0]], out)
    if stack:  # 出栈，之后慢慢入栈
        dfs(wait, stack[:-1], out + [stack[-1]])


n, nums = int(input()), list(map(int, input().split()))

dfs(nums, [], [])
for i in sorted(res):
    print(i)
