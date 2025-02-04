class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        res = 0
        flag = False
        for num, count in d.items():
            if count % 2 == 0:
                res += count
            else:
                flag = True
                res += count - 1
        
        if flag:
            res += 1
        
        return res