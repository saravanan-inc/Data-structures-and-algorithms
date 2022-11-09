arr = [1, 2, 3, 4, 5]

target = 3

start = 0
end = 1

while end < target:
    temp = end
    end = end + end-start+1
    start = temp

while start <= end:
    mid = start + ((end - start)//2)

    if target < arr[mid]:
        end = mid - 1

    elif target > arr[mid]:
        start = mid + 1

    else:
        print(arr[mid], target)
        break
