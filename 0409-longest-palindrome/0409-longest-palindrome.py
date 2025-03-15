class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = defaultdict(int)
        for i in s:
            d[i] += 1
        flag = 0
        res = 0
        for i in d:
            if d[i] % 2:
                flag = 1
                res += d[i] - 1
            else:
                res += d[i]
        
        if flag == 1:
            res += 1
        
        return res