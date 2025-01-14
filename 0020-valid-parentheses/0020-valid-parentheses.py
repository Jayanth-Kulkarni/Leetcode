class Solution:
    def isValid(self, s: str) -> bool:
        valid = {"{": "}", "[": "]", "(": ")"}
        stack = []
        for i in s:
            if i in valid:
                stack.append(i)
            elif len(stack) > 0 and i == valid[stack[-1]]:
                stack.pop(-1)
            else:
                return False
        if len(stack) == 0:
            return True
        return False