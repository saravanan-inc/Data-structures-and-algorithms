from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        
        pivot = 0
        
        while start <= end:
            mid = start+(end-start)//2
            
            if mid < end and nums[mid] > nums[mid+1]:
                pivot = mid
                break
            
            if mid > start and nums[mid] < nums[mid-1]:
                pivot = mid
                break
                
            if nums[mid] >= nums[start]:
                start = mid+1
            else:
                end = mid-1
                
                
        if nums[pivot] == target:
            return pivot
        
        ans1 = self.binarySearch(0, pivot-1, nums, target)
        
        if ans1 == -1:
            return self.binarySearch(pivot+1, len(nums)-1, nums, target)
        
    def binarySearch(self, start: int, end: int, nums: List[int], target: int):
        
        while start <= end:
            mid = start + (end-start)//2
            print(start, end, mid)
            
            if (target == nums[mid]):
                return mid
            if (target > nums[mid]):
                start = mid + 1
            else:
                end = mid - 1
            
        return -1

print(Solution().search(
[3,1]
,1))