class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        sign = 1
        res = 0
        for i in range(len(s)):
            if i==0 and s[i] == "-":
                sign = -1
                continue
            if i==0 and s[i] == "+":
                continue
            if s[i].isdigit():
                res = res * 10 + int(s[i])
            else:
                break
        res = res * sign
        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif res < -2 ** 31:
            return -2 ** 31
        else:
            return res