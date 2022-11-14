from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start = 0
        end = len(letters)-1

        while start <= end:
            mid = start + (end-start)//2

            if letters[mid] > target:
                end = mid-1
            else:
                start = mid+1

        print(start)
        return letters[start % len(letters)]


s = Solution().nextGreatestLetter(["c", "f", "j"], 'a')

print(s)
