array = [4, 3, 1, 2, 6, 8]

for i in range(len(array)):
    for j in range(0, len(array)-i-1):
        if array[j] > array[j+1]:
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp

print(array)
