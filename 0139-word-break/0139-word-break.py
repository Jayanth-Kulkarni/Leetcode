class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # loop through reverse s and see if worddict 
        n = len(s)
        dp = [False for i in range(n+1)]
        dp[n] = True
        for i in range(n-1,-1,-1):
            for word in wordDict:
                if i+len(word) <= len(s) and s[i:i+len(word)] == word:
                    dp[i] = dp[i+len(word)]
                if dp[i]:
                    break
        
        return dp[0]