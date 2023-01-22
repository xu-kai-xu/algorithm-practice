
# n = 5
# nums = [1, 2, 3, 1, 4]

n = 2
nums = [1, 2]


distance = -1
i = 0

while i< len(nums):
    for j in range(i+1, len(nums)):
        if nums[i] == nums[j]:
            distance = max(j - i, distance)
    i += 1

print(distance)

#=======================
raw = '2 5 1 0'

settings = [int(i) for i in raw.split(' ')]

# 场地尺寸 x y
x = settings[0]
y = settings [1]


# 电站尺寸 m n
if len(settings) == 4:
    m = n = settings[2]
else:
    m = settings[2]
    n = settings[3]

min_power = settings[-1]
total = 0


lands =[[1, 3, 4, 5, 8],
        [2, 3, 6, 7, 1]]


for i in range(x-m+1):
    tmp = lands[i:i+m]

    for j in range(y-n+1):
        choose = []
        for row in tmp:
            choose.append(sum(row[j:j+n]))
        power = sum(choose)
        if power >= min_power:
            total += 1




#=====================
n = 4
total = [[1, 1, 0, 0], [1, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]]


corr = {}
for i in range(n):
    corr[i] = []
    for j in range(n):
        if total[i][j] == 1:
            corr[i].append(j)

linux = []
for i in range(n):
    tmp = set(corr[i])
    for j in range(n):
        if j == i:
            continue
        intersection = tmp.intersection(set(corr[j]))
        if intersection:
            tmp.add(j)

    linux.append(tmp)


res = [len(item) for item in linux]

res.sort(reverse=True)

print(res[0])











