from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        for g in grid:
            start = 0
            end = len(g)
            found = False
            while start < end:
                mid = start + (end-start)//2

                if g[mid] >= 0:
                    start = mid+1
                else:
                    found = True
                    end = mid

            if found:
                ans += len(g) - start

        return ans


# Solution().countNegatives([[3, 2], [1, 0]])
print(Solution().countNegatives([[3, 2], [1, 0]]))
