from typing import List


# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         start = 0
#         end = len(numbers)

#         while start < end:
#             m = numbers[start] + numbers[end]

#             if m == target:
#                 return [start+1, end+1]
#             elif m < target:
#                 start += 1
#             else:
#                 end -= 1


# s = Solution()
# print(s.twoSum([2, 3, 4], 6))

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            posAns = target-numbers[i]
            start = 0
            end = len(numbers)-1
            
            while start <= end:
                mid = start + (end-start)//2
                
                if mid != i and numbers[mid] == posAns:
                    return [i+1, mid+1]
                
                if numbers[mid] > posAns:
                    end = mid-1
                else:
                    start = mid+1
                
s = Solution()
print(s.twoSum([2, 3, 4], 6))