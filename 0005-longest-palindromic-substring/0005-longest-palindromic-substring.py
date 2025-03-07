class Solution:
    def longestPalindrome(self, s: str) -> str:
        reslen = -float("inf")
        res = ""
        for i in range(len(s)):
            p, q = i, i
            while 0 <= p <= q < len(s) and s[p] == s[q]:
                if reslen < q-p+1:
                    reslen = q-p+1
                    res = s[p:q+1]
                p -= 1
                q += 1

            p, q = i, i+1
            while 0 <= p <= q < len(s) and s[p] == s[q]:
                if reslen < q-p+1:
                    reslen = q-p+1
                    res = s[p:q+1]
                p -= 1
                q += 1
        return res