"""
将两个升序数组合并为一个新的数组并返回。新数组满足数组头节点值不小于数组尾节点值，
去掉数组头尾节点，剩余数组依然满足数组头节点值不小于数组尾节点值，依次递推。

示例 1：
输入：l1 = [1,2,4], l2 = [1,3,5]
输出：[1，3，5，4，2，1]

示例 2：
输入：l1 = [5, 10, 15], l2 = [20, 40]
输出：[10，20，40，15，5]
"""

L1 = [1,2,4]
L2 = [1,3,5]

# L1 = [5, 10, 15]
# L2 = [20, 40]

res1 = []
res2 = []

L1 = L1[::-1]
L2 = L2[::-1]

while True:
    if L1[-1] <= L2[-1]:
        res2.append(L1.pop())
    else:
        res2.append(L2.pop())

    if (len(L1) == 0) or (len(L2) == 0):
        break

    if L1[-1] <= L2[-1]:
        res1.append(L1.pop())
    else:
        res1.append(L2.pop())


if (len(L1) == 0) and (len(L2) != 0):
    while True:
        if L2[0] <= L2[-1]:
            res1.append(L2[0])
            L2.remove(L2[0])
        else:
            res1.append(L2[-1])
            L2.remove(L2[-1])

        if len(L2) == 0:
            break

        if L2[0] <= L2[-1]:
            res2.append(L2[0])
            L2.remove(L2[0])
        else:
            res2.append(L2[-1])
            L2.remove(L2[-1])

        if len(L2) == 0:
            break


if (len(L2) == 0) and (len(L1) != 0):
    while True:
        if L1[0] <= L1[-1]:
            res1.append(L1[0])
            L1.remove(L1[0])
        else:
            res1.append(L1[-1])
            L1.remove(L1[-1])

        if len(L1) == 0:
            break

        if L1[0] <= L1[-1]:
            res2.append(L1[0])
            L1.remove(L1[0])
        else:
            res1.append(L1[-1])
            L1.remove(L1[-1])

        if len(L1) == 0:
            break

res = res1.extend(res2[::-1])






