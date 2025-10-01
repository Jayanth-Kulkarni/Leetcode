class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        remainder = float("inf")
        res = numBottles
        while remainder >= numExchange:
            remainder = int(numBottles/numExchange) + numBottles%numExchange
            res += int(numBottles/numExchange)
            numBottles = remainder
        return res