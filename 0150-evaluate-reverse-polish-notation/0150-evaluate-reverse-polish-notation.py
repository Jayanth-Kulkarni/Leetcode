class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = list("+-*/")
        stack = []
        for token in tokens:
            if token not in op:
                stack.append(int(token))
            else:
                second, first = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(first + second)
                elif token == "-":
                    stack.append(first - second)
                elif token == "*":
                    stack.append(first * second)
                elif token == "/":
                    stack.append(int(first / second))
        return stack[0]
