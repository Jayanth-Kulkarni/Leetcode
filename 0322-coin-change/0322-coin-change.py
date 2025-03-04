class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf") for i in range(amount+1)]
        dp[0] = 0
        for a in range(amount+1):
            for c in coins:
                if a-c >= 0:
                    dp[a] = min(1+dp[a-c], dp[a])
        return dp[amount] if dp[amount] != float("inf") else -1