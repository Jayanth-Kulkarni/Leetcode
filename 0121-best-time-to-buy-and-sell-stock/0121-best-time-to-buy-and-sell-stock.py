class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = -1
        min_val = math.pow(10,4)+1
        for price in prices:
            min_val = min(price,min_val)
            max_profit = max(max_profit,price-min_val)
        return max_profit
            