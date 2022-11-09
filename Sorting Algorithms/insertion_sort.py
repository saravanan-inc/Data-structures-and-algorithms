array = [4, 3, 1, 2, 6, 8]


def swap(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp


for i in range(len(array)):
    j = i+1

    while j > 0 and j < len(array)-1:
        if array[j] < array[j-1]:
            swap(array, j, j-1)
            j -= 1
        else:
            break


print(array)
