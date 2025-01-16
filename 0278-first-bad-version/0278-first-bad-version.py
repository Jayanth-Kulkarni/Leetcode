# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n-1
        low = n
        while l <= r < n:
            m = (l+r)//2
            if isBadVersion(m):
                low = m
                r = m-1
            else:
                l = m+1

        return low