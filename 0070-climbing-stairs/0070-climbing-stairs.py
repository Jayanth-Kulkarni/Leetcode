class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0 for i in range(n+1)]
        res[n] = 1
        res[n-1] = 1
        for i in reversed(range(0,n-1)):
            res[i] = res[i+1] + res[i+2]
        return res[0]