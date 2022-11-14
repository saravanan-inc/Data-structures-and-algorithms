class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start = 0
        end = num//2

        while start < end:
            mid = start + (end-start)//2

            if mid * mid == num:
                return True
            elif mid * mid > num:
                end = mid-1
            else:
                start = mid+1

        return False


s = Solution()
print(s.isPerfectSquare(16))
