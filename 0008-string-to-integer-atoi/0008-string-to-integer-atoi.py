class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        sign = 1
        res = 0
        for idx, i in enumerate(s):
            if idx == 0 and i == "+":
                continue
            if idx == 0 and i == "-":
                sign = -1
                continue
            if i.isdigit():
                res = res * 10 + int(i)
            else:
                break
        
        res = sign * res
        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        
        if res < -2 ** 31:
            return -2 ** 31
        
        return res