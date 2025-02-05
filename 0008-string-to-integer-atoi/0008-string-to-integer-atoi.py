class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        sign = 1
        parsed = 0

        for idx, c in enumerate(s):
            if idx == 0 and c == "-":
                sign = -1
                continue
            if idx == 0 and c == "+":
                continue
            if not c.isdigit():
                break
            parsed = 10 * parsed + int(c)
        
        if sign == -1:
            parsed = -parsed

        if parsed > 2**31-1:
            return  2**31-1
        elif parsed < -2**31:
            return  -2**31
        
        return parsed