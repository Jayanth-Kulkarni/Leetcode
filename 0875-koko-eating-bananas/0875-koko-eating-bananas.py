class Solution:
    def findSpeed(self,piles,h,k):
        hours = 0
        for i in piles:
            hours += math.ceil(i/k)
        if hours>h:
            return False
        return True 


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        while l<r:
            mid = (l+r)//2
            if self.findSpeed(piles,h,mid):
                r = mid
            else:
                l = mid+1
        return l