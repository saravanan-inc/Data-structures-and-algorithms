from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        start = 0
        end = len(nums)

        while start < end:
            mid = start + (end-start)//2

            if nums[mid] > mid:
                end = mid

            else:
                start = mid+1

        return start
