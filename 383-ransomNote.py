# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 07:26:04 2023

@author: xuk11

383- 赎金信
"""

ransom1 = 'a'
magazin1 = 'b'

ransom2 = 'aa'
magazin2 = 'ab'

ransom3 = 'aa'
magazin3 = 'aab'


def canConstruct(ransomNote, magazine):
    hash_table =[0] * 26
    for letter in magazine:
        hash_table[ord(letter) - 97] += 1
    for letter in ransomNote:
        hash_table[ord(letter) - 97] -= 1

    for count in hash_table:
        if count < 0:
            return False
    return True

canConstruct(ransom1, magazin1)
canConstruct(ransom2, magazin2)
canConstruct(ransom3, magazin3)
