class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [float("inf") for i in range(n+1)]
        dp[n], dp[n-1] = 1, 1
        for i in reversed(range(n-1)):
            dp[i] = dp[i+1] + dp[i+2]
        
        return dp[0]