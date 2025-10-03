class Solution:
    def findSpeed(self, piles, k, h):
        sum = 0
        for pile in piles:
            sum += math.ceil(pile/k)
        if sum <= h:
            return True
        return False


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Do binary search here
        l, r = 1, max(piles)
        res = r
        while l < r:
            mid = (l+r)//2
            if self.findSpeed(piles, mid, h):
                res = mid
                r = mid
            else:
                l = mid + 1
        return res