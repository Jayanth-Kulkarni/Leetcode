class Solution:
    def findspeed(self,piles,h,k):
        speed = 0
        for pile in piles:
            speed += math.ceil(pile/k)
        if speed > h:
            return False
        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = 1
        while l <= r:
            mid = (l + r)//2
            if self.findspeed(piles, h, mid):
                r = mid-1
                res = mid
            else:
                l = mid+1
        return res