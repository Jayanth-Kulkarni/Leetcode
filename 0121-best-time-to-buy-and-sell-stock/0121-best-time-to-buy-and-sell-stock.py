class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, minprice = 0, float("inf")
        for price in prices:
            minprice = min(price, minprice)
            res = max(res, price - minprice)
        return res