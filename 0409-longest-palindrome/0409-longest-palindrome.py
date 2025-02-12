class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for i in s:
            d[i] = 1 + d.get(i, 0)
        flag = False
        count = 0
        for key in d:
            if d[key] % 2==0:
                count += d[key]
            else:
                flag = True
                count += d[key] - 1
        
        if flag:
            count += 1
        
        return count