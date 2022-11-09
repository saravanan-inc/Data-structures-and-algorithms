array = [4, 3, 1, 2, 6, 8]


def swap(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp


for i in range(len(array)):
    min = i
    for j in range(i, len(array)-1):
        if array[min] > array[j]:
            min = j
    if min != i:
        swap(array, i, min)

print(array)
