arr = [1, 2, 3, 4, 5]

target = 4

start = 0
end = len(arr)-1

while start < end:
    mid = start + ((end - start)//2)
    print(mid)

    if target < arr[mid]:
        end = mid - 1

    elif target > arr[mid]:
        start = mid + 1

    else:
        print(arr[mid], target)
        break
