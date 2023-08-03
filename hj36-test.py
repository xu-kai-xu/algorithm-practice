# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 09:40:39 2022

@author: xuk11
"""
key = 'nihhao'
text = 'ni'

old = [chr(i) for i in range(97, 123)]

new = []
for s in key:
    if s not in new:
        new.append(s)

for m in old:
    if m not in new:
        new.append(m)