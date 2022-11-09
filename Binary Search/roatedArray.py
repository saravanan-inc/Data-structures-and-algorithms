arr = [3, 2, 1, 0, 5, 4]

start = 0
end = len(arr)-1

target = 3


def search(arr, start, end, target, isLeft):
    ans = -1
    while start <= end:
        mid = start + ((end - start)//2)

        if target == arr[mid]:
            ans = mid
            break

        if isLeft:
            if target > arr[mid]:
                start = mid+1
            elif target < arr[mid]:
                end = mid-1
        else:
            if target > arr[mid]:
                end = mid-1
            elif target < arr[mid]:
                start = mid+1

    return ans


while start < end:
    mid = start + ((end - start)//2)

    if arr[mid] > arr[mid+1]:
        end = mid
    else:
        start = mid+1

left = search(arr, 0, end, target, True)
right = search(arr, end, len(arr)-1, target, False)

print(left, right)
