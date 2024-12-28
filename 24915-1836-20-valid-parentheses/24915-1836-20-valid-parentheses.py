class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {"(":")", "{":"}", "[":"]"}
        stack =  []
        for i in s:
            if i in bracket:
                stack.append(i)
            elif len(stack)>0 and i == bracket[stack[-1]]:
                stack.pop()
            else:
                return False
        if len(stack) > 0:
            return False
        return True 