class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = float("inf")
        max_profit = 0
        for price in prices:
            min_val = min(price, min_val)
            max_profit = max(max_profit, price - min_val)
        return max_profit