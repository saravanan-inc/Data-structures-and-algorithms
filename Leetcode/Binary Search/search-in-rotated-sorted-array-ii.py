from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def findPivot():
            start = 0
            end = len(nums)-1

            while start <= end:
                mid = (start+end)//2

                if mid > start and nums[mid-1] > nums[mid]:
                    return mid-1

                if mid < end and nums[mid+1] < nums[mid]:
                    return mid

                if nums[mid] >= nums[start] and nums[mid] != nums[end]:
                    start = mid+1
                elif nums[mid] <= nums[start]  and nums[mid] != nums[end]:
                    end = mid-1
                else:
                    if start < end and nums[start] > nums[start+1]:
                        return start
                    elif start > 0 and nums[start] < nums[start-1]:
                        return start-1
                    else:
                        start+=1
                    if end < len(nums)-1 and nums[end] > nums[end+1]:
                        return end
                    elif end > start and nums[end] < nums[end-1]:
                        return end-1
                    else:
                        end-=1
                    

            return -1
            
        def binarySearch(start, end):
            while start <= end:
                mid = start + (end-start)//2
                if nums[mid] == target:
                    return True
                
                if nums[mid] > target:
                    end = mid-1
                else:
                    start = mid+1
            return False
        
        p = findPivot()

        if p == -1:
            return binarySearch(0, len(nums)-1)

        if nums[p] == target:
            return True

        a1 = binarySearch(0, p-1)
        
        if a1: return a1
        return binarySearch(p+1, len(nums)-1)

print(Solution().search([1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1], 3))      
