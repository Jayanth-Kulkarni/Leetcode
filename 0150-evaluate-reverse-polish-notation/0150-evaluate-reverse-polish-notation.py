class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set("+-*/")
        stack = []
        for token in tokens:
            if token in operators:
                second = stack.pop()
                first = stack.pop()
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