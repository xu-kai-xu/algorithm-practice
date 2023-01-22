# 冒泡排序

def bubble_sort(array):
    array_length = len(array)
    if array_length <= 1:
        return
    for i in range(array_length):
        for j in range(array_length - i - 1):
            flag = False
            if array[j] > array[j+1]:
                # tmp = array[j]
                # array[j] = array[j+1]
                # array[j+1] = tmp
                array[j], array[j+1] = array[j+1], array[j]
                flag = True
        if not flag:
            break
    
test1 = [2, 3, 4, 1, 6, 4, -1]
test2 = [9, 8, 6, 5, 6, 7, 2, 1, 0]
print(test1, '\n', test2, '\n')
bubble_sort(test1)
bubble_sort(test2)
print(test1, '\n', test2)
