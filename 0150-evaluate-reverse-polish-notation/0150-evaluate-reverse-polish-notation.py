class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = list("+-*/")
        stack = []
        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                if len(stack) < 2:
                    return False
                second, first = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(first + second)
                elif token == "-":
                    stack.append(first - second)
                elif token == "/":
                    stack.append(int(first / second))
                else:
                    stack.append(first * second)
        return stack[0]