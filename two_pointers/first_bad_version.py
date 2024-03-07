# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        count = 0
        first,last = 1,n
        while first<last:
            mid = (first+last)//2
            count+=1
            print(mid,count)
            if is_bad_version(mid):
                last = mid
            else:
                first = mid+1
        return first, count