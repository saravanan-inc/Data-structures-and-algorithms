from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        map = {}

        for i in nums1:
            if i in map:
                map[i] = map[i]+1
            else:
                map[i] = 1

        for j in nums2:
            if j in map and map[j] > 0:
                ans.append(j)
                map[j] = 0

        return ans


Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4])
