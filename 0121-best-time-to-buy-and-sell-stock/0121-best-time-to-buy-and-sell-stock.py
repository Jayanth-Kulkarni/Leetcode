class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = float("inf")
        max_profit = 0
        for price in prices:
            profit = price - min_val
            min_val = min(min_val, price)
            max_profit = max(max_profit, profit)
        return max_profit