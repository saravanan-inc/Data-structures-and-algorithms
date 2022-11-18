from typing import List


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum1 = 0
        sum2 = 0

        for i in aliceSizes:
            sum1 += i

        for j in bobSizes:
            sum2 += j

        mid = (sum1+sum2)//2

        start = 0
        end = len(bobSizes)-1

        while (start <= len(aliceSizes)-1 and end >= 0):
            if aliceSizes[start]+bobSizes[end] == mid:
                return [aliceSizes[start], bobSizes[end]]

            if aliceSizes[start] > mid and len(aliceSizes)-1 > start+1:
                start += 1
            else:
                end -= 1


print(Solution().fairCandySwap([2], [1, 3]))
