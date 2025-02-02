class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = list("+-*/")
        for token in tokens:
            if token in operations:
                if len(stack) < 2:
                    return False
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