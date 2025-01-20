class Solution:
    def longestPalindrome(self, s: str) -> int:
        d_s = defaultdict(int)
        for i in s:
            d_s[i] += 1
        
        res = 0
        odd = False
        for i in d_s:
            if d_s[i] % 2 == 0:
                res += d_s[i]
            else:
                res += d_s[i] - 1
                odd = True
        
        if odd:
            res += 1
        
        return res