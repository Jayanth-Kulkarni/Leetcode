class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = list("+-*/")
        stack = []
        for token in tokens:
            if token in operator:
                second, first = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(first + second)
                if token == "-":
                    stack.append(first - second)
                if token == "*":
                    stack.append(first * second)
                if token == "/":
                    stack.append(int(first / second))
            else:
                stack.append(int(token))
            
        return stack[0]