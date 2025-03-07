class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip(" ")
        res = 0
        sign = 1
        for idx, i in enumerate(s):
            if idx == 0 and i == "-":
                sign = -1
                continue
            elif idx == 0 and i == "+":
                continue
            if i.isdigit():
                res = res * 10 + int(i)
            else:
                break
        
        if sign == -1:
            res = sign * res
        
        if res < - 2 ** 31:
            return - 2 ** 31
        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        
        return res
