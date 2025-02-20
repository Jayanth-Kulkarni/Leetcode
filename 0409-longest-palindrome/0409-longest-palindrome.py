class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = defaultdict(int)
        for i in s:
            d[i] += 1
        res = 0
        flag = 0
        for i in d:
            if d[i] % 2 == 0:
                res += d[i]
            
            else:
                flag = 1
                res += d[i] - 1
        
        if flag:
            res += 1
        
        return res