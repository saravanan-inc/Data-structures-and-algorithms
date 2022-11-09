arr = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]

start = 0
end = len(arr)-1

while start < end:
    mid = start + ((end - start)//2)

    if arr[mid] > arr[mid+1]:
        end = mid
    else:
        start = mid+1

print(start, end)
