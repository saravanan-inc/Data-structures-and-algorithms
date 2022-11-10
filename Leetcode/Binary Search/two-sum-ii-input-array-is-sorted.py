from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers)

        while start < end:
            m = numbers[start] + numbers[end]

            if m == target:
                return [start+1, end+1]
            elif m < target:
                start += 1
            else:
                end -= 1


s = Solution()
print(s.twoSum([2, 3, 4], 6))
