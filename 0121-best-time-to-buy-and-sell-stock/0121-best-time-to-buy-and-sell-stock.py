class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minval = prices[0]
        res = 0
        for price in prices[1:]:
            minval = min(minval, price)
            res = max(res, price - minval)
        return res