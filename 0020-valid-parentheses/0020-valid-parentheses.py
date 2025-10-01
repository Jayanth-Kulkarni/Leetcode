class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closes = {"{":"}", "[":"]", "(":")"}
        for ch in s:
            if ch in closes:
                stack.append(ch)
            elif len(stack) > 0 and closes[stack[-1]] == ch:
                stack.pop()
            else:
                return False
        return len(stack) == 0