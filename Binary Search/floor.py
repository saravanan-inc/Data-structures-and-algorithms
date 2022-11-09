arr = [1, 2, 3, 5]

target = 4

start = 0
end = len(arr)-1

while start <= end:
    mid = start + (end - start//2)

    if target < arr[mid]:
        end = mid - 1

    else:
        start = mid + 1

print(arr[end])
