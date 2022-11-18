from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()

        for i in range(0, len(arr)-1):
            target = 2*arr[i]
            start = 0
            end = len(arr)

            while start < end:
                mid = start+(end-start)//2

                if arr[mid] > target:
                    end = mid-1
                elif arr[mid] < target:
                    start = mid+1
                else:
                    return True

        return False


print(Solution().checkIfExist([10, 5, -9, 15, 3, 8, 12, -10]))
