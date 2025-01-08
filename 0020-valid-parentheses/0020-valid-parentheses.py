class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(": ")", "{" : "}", "[" : "]"}
        stack = []
        for i in s:
            if i in d:
                stack.append(i)
            elif len(stack) > 0 and i == d[stack[-1]]:
                stack.pop()
            else:
                return False
        return True if len(stack) == 0 else False