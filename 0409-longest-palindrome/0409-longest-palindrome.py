class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        res = 0
        isodd = False
        for key, val in d.items():
            if val%2 != 0:
                res += val-1
                isodd = True
            else:
                res += val

        if isodd:
            res += 1
        
        return res