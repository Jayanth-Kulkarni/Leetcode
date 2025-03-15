class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        sign = 1
        s = s.lstrip()
        for i in range(len(s)):
            print(i, s[i])
            if i == 0 and s[i] == "-":
                sign = -1
                continue
            elif i == 0 and s[i] == "+":
                sign = 1
                continue
            elif s[i].isdigit() != True:
                break
            
            res = res * 10 + int(s[i])
        
        if sign == -1:
            res = -1 * res
        
        if -2**31 > res :
            return -2**31
        
        if res > 2**31 - 1:
            return 2**31 - 1
        
        return res