class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = math.pow(10,5) + 1
        max_profit = -1
        for price in prices:
            min_price = min(price,min_price)
            max_profit = max(max_profit, price-min_price)
        return max_profit
