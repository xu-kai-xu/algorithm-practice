# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 20:42:32 2022

@author: xuk11
"""
# a = 'abcdefghijklmnopa'
# b = 'abcsafjklmnopqrstuvw'
# a = 'efgyiffxoonftmmvd'
# b = 'exwzdcwjsttuhsxrcpzplpnfqxqsqtlfctdkgacejitayoafucmfxxhkxyixxykndchyjc'

a = 'yrtqyfxyrmbasfmkbuudetaahxxgvcpkfhlkfxtjvguizsmwbnwamftshffyzumqfzqvirxgjjuocobvhvgstvrynduavkvntvxgnravjyfjkycguqyrnbnwnoqvhh'
b = 'xxzjrwyqtgzfgxyitvszmltcsdjweeycqgzsazahpqrvlgvwexcfwkusmuyltvtbjftkvwebmjctwbfcxfimoevbquznojlzkxygruhebhostshenguhymzjxhkjstiwzgyudtfeddgqlegxesngnlbubkhzfmspalfajiqsvohghxhswjiimnyazfmgqazdewfptldiilrwkhuntvseohykutjecuhg'

if len(a) > len(b):
    a, b = b, a


res = []
size = len(a)
tmp = ''
i = 0

while i < size:
    tmp += a[i]
    if tmp in b:
        pass
    elif (tmp not in b) and (len(tmp)) > 1:
        res.append(tmp[:-1])
        tmp = ''
        i -= 1
    i += 1


if tmp != '':
    res.append(tmp)

sorted(res, key=lambda x: len(x), reverse=True)[0]