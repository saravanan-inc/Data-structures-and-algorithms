arr = [1, 2, 2, 2, 2, 3, 4, 5]

target = 2


def search(arr, isLeft):
    start = 0
    end = len(arr)-1

    ans = -1

    while start <= end:
        mid = start + ((end - start)//2)

        if target < arr[mid]:
            end = mid - 1

        elif target > arr[mid]:
            start = mid + 1

        else:
            ans = mid

            if isLeft:
                end = mid-1
            else:
                start = mid+1

    return ans


left = search(arr, True)
right = search(arr, False)

print([left, right])
