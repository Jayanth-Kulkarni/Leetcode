class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, float("inf")
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(price - min_price, max_profit)
        return max_profit