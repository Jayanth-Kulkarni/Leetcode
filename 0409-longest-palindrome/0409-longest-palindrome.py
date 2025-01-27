class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = defaultdict(int)
        for i in s:
            d[i] += 1
        
        res = 0
        isodd = False
        for i, r in d.items():
            if r % 2 == 0:
                res += r
            else:
                res += r-1
                isodd = True
        
        if isodd:
            res += 1
        
        return res
        
