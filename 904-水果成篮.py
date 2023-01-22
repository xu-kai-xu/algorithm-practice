
def totalFruit(fruits):
    start = 0
    res = 0
    length = 0
    size = len(fruits)
    tmp = []

    for i in range(size):
        tmp.append(fruits[i])
        num = len(set(tmp))
        length = i - start + 1
        while num > 2:
            tmp.remove(fruits[start])
            num = len(set(tmp))
            length -= 1
            start += 1
        if res < length:
            res = length


    return res

#fruits = [3,3,3,1,2,1,1,2,3,3,4]
#fruits = [1, 2, 1]
#fruits = [0,1,2,2]
t = totalFruit(fruits)
print(t)