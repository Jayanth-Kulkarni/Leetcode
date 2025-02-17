class Solution:
    def longestPalindrome(self, s: str) -> str:
        reslen = 0
        res = ""
        for i in range(len(s)):
            # odd
            l, r = i, i
            while 0 <= l <= r < len(s) and s[l] == s[r]:
                if reslen < r - l + 1:
                    reslen = r - l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1
            # even
            l, r = i, i+1
            while 0 <= l <= r < len(s) and s[l] == s[r]:
                if reslen < r - l + 1:
                    reslen = r - l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1
        return res