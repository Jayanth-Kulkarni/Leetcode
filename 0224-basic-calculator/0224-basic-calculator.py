class Solution:
    def calculate(self, s: str) -> int:
        res, cur_num, sign, stack = 0, 0, 1, []
        for c in s:
            if c.isdigit():
                cur_num = cur_num * 10 + int(c)
            
            elif c in "+-":
                res += cur_num * sign
                cur_num = 0
                sign = 1 if c == "+" else -1
            
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1
            
            elif c == ")":
                res += cur_num * sign
                res *= stack.pop()
                res += stack.pop()
                cur_num = 0
        
        return res + (cur_num * sign)