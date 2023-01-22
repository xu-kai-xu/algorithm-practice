# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 16:34:38 2022

@author: xuk11

https://www.nowcoder.com/practice/2baa6aba39214d6ea91a2e03dff3fbeb?tpId=37&tqId=21241&rp=1&ru=%2Fexam%2Foj%2Fta&qru=%2Fexam%2Foj%2Fta&sourceUrl=%2Fexam%2Foj%2Fta%3FtpId%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=

算法分析 功能分析
1. 循环记录，最多只记录8条，当记录数超过8时，弹出第一个；
2.不输出文件所在路径，文件名大于16位时，只输出16位字符；
3. 计数，文件名和错误行相同，视为相同的错误记录；
4. 记录顺序以第一次出现的顺序为准；

数据结构：
1. 使用 collections.Counter
2. 键使用（文件名，错误行），
3. 值为记录数，
4. 保留字典第一个键，超过8条记录后就删除第一个，循环操作，
5. 如何获取字典第一个键，
6. 有效信息提取——正则表达
"""
from collections import Counter
raw = [['D:\\zwtymj\\xccb\\ljj\\cqzlyaszjvlsjmkwoqijggmybr', '645'],
       ['E:\\je\\rzuwnjvnuz', '633'],
       ['C:\\km\\tgjwpb\\gy\\atl', '637'],
       ['F:\\weioj\\hadd\\connsh\\rwyfvzsopsuiqjnr', '647'],
       ['E:\\ns\\mfwj\\wqkoki\\eez', '648'],
       ['D:\\cfmwafhhgeyawnool', '649'],
       ['E:\\czt\\opwip\\osnll\\c', '637'],
       ['G:\\nt\\f', '633'],
       ['F:\\fop\\ywzqaop', '631'],
       ['F:\\yay\\jc\\ywzqaop', '631'],
       ['D:\\zwtymj\\xccb\\ljj\\cqzlyaszjvlsjmkwoqijggmybr', '645']]


def mesg_parse(err_msg):
    """
    parse err_msg
    input: list, [raw file name line_num]
    return: tuple (f_name, line_num)
    """
    line = err_msg[1]
    rf = (err_msg[0]).split('\\')[-1]
    if len(rf) > 16:
        f_name = rf[-16:]
    else:
        f_name = rf
    return((f_name, line))


keys = [mesg_parse(item) for item in raw]

cnt = Counter()
for item in keys:
    cnt[item] += 1


for line in list(cnt.items())[-8:]:
    print(line[0][0], line[0][1], line[1], sep=' ')

