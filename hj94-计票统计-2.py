# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 09:53:18 2022

@author: xuk11
"""
#不用 counter 自己实现

n_cand = 4
names_cand = 'A B C D'.split(' ')
n_poll = 8
polls = 'A D E CF A GG A B'.split(' ')

c = dict()
for name in names_cand:
    c[name] = 0
c['Invalid'] = 0

for poll in polls:
    if poll in names_cand:
        c[poll] += 1
    else:
        c['Invalid'] += 1

for name in names_cand:
    print(name, ':', c[name])
print('Invalid', ':', c['Invalid'])



