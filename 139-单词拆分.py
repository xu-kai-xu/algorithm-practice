# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 10:25:38 2022

@author: xuk11
"""

import re

# s = "leetcode"
# wordDict = ["leet", "code"]

# s = "applepenapple"
# wordDict = ["apple", "pen"]

# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]

s = "cars"
wordDict = ["car","ca","rs"]

def wordBreak(s, wordDict):
    strs = s
    # flag 标记s中是否有与wordDict相匹配的单词
    flag = [True for word in wordDict]

    while True in flag:  # 当全无匹配时结束循环
        for i, word in enumerate(wordDict):
            if re.search(word, strs):
                strs = re.sub(word, '', strs)
                flag[i] = True
            else:
                flag[i] = False

    if strs == '':
        return True
    else:
        return False


wordBreak(s, wordDict)
