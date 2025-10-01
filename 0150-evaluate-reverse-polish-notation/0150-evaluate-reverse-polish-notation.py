class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token in "+*-/":
                a,b = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(a+b)
                if token == "-":
                    stack.append(b-a)
                if token == "*":
                    stack.append(a*b)
                if token == "/":
                    stack.append(int(b/a))
            else:
                stack.append(int(token))
        return stack[-1]