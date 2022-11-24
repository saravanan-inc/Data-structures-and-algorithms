from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            start = 0
            end = len(i)-1
            
            while start <= end:
                mid = start + (end-start)//2
                if i[mid] < target:
                    start = mid+1
                elif i[mid] > target:
                    end = mid-1
                else:
                    return True
        return False

print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))