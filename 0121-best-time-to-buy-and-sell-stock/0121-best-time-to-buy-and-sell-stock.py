class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minval = float("inf")
        for price in prices:
            if price < minval:
                minval = price
            maxprofit = max(maxprofit, price - minval)
        return maxprofit