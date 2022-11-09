def heapify(array, n, i):
    print("i-array", i, array)
    l = i
    left = i*2+1
    right = i*2+2

    if left < n and array[left] > array[l]:
        l = left

    if right < n and array[right] > array[l]:
        l = right

    if l != i:
        temp = array[l]
        array[l] = array[i]
        array[i] = temp


def insert(array, value):
    array.append(value)

    if len(array) > 2:
        for i in range(0, (len(array)-1//2)-1):
            heapify(array, len(array)-1, i)


arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)

print(arr)
