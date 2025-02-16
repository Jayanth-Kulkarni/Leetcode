class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = defaultdict(int)
        for i in s:
            d[i] += 1
        res = 0
        flag = False
        print(d)
        for i in d:
            if d[i] % 2:
                print(i, res)
                flag = True
                res += d[i] - 1
            else:
                res += d[i]
        if flag:
            res += 1
        
        return res