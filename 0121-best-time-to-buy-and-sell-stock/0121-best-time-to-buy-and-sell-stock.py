class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # save max_profit as -1, take the min_val as the first element
        # run a loop over all the prices and find the difference between the min_val and price
        # and calculate the max of the 2. Return max after the loop

        max_profit = -1
        min_val = prices[0]
        for price in prices:
            profit = price - min_val
            min_val = min(min_val, price)
            max_profit = max(max_profit, profit)
        
        return max_profit