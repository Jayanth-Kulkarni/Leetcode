class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 0
        resstr = ""
        for i in range(len(s)):
            # odd
            l, r = i, i+1
            while 0 <= l <= r < len(s) and s[l] == s[r]:
                if r-l+1 > res:
                    res = r-l+1
                    resstr = s[l:r+1]
                l = l - 1
                r = r + 1
                
            # even
            l, r = i, i
            while 0 <= l <= r < len(s) and s[l] == s[r]:
                if r-l+1 > res:
                    res = r-l+1
                    resstr = s[l:r+1]
                l = l - 1
                r = r + 1
        
        return resstr