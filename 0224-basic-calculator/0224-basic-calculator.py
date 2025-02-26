class Solution:
    def calculate(self, s: str) -> int:
        cur, res, sign, stack = 0, 0, 1, []
        for i in s:
            if i.isdigit():
                cur = cur * 10 + int(i)
            elif i in "+-":
                res += cur * sign
                cur = 0
                sign = 1 if i == "+" else -1
            
            elif i == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1

            elif i == ")":
                res += cur * sign
                res *= stack.pop()
                res += stack.pop()
                cur = 0
            

        return res + (cur * sign)