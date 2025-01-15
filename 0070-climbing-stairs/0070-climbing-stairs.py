class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[n] = 1
        dp[n-1] = 1
        for i in reversed(range(0,n-1)) :
            dp[i] = dp[i+1] + dp[i+2]
        return dp[0]