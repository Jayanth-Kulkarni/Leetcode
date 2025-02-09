class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        flag = 1
        res = 0
        for idx, i in enumerate(s):
            if idx == 0 and i == "-":
                flag = -1
                continue
            elif idx == 0 and i == "+":
                continue
            
            if not i.isdigit():
                break
            
            res = res * 10 + int(i)

        if flag == -1:
            res = -1 * res

        if res > 2**31 - 1:
            return 2**31 - 1
        elif res < -2**31:
            return -2**31
        return res