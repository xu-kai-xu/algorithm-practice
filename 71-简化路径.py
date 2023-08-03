# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 07:33:55 2023

@author: xuk11
71 简化路径
"""
path1 = "/home/"
path2 = "/../"
path3 = "/home//foo/"
path4 = "/a/./b/../../c/"
path5 = "/a/../../b/../c//.//"
path6 = "/a//b////c/d//././/.."


def remove_multi_slash(path):
    res = []
    res.append(path[0])  # 先添加一个元素进去
    for item in path[1:]:
        if res[-1] == '/' and item == '/':
            continue
        else:
            res.append(item)

    return ''.join(res)


def split_slash(path):
    flag = False  # 指示是否读到了第二个slash
    res = []
    for item in path:
        if item == '/' and flag == False:
            tmp = ''  # 初始化存放路径名称的临时变量
            continue
        elif item == '/' and flag == True:
            res.append(tmp)
            flag = False
            tmp = ''
            continue
        else:  # 获取路径名字
            tmp += item
            flag = True

    if tmp:
        res.append(tmp)

    return res


def simplifyPath(path):
    new_path = remove_multi_slash(path)  # 删掉重复 /
    path_list = split_slash(new_path)

    res = []
    for name in path_list:
        if name == '.':
            continue
        elif name == '..':
            try:
                res.pop()
            except IndexError:
                pass
        else:
            res.append(name)

    return '/' + '/'.join(res)


t = remove_multi_slash(path6)
t2 = split_slash(t)
simplifyPath(path6)
