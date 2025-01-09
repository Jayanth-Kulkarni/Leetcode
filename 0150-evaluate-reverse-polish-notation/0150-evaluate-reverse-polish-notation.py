class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        symbols = set("+-*/")
        stack = []
        for i in tokens:
            if i in symbols:
                second, first = stack.pop(), stack.pop()
                if i == "+":
                    stack.append(first + second)
                if i == "-":
                    stack.append(first - second)
                if i == "*":
                    stack.append(first * second)
                if i == "/":
                    stack.append(int(first / second))
            else:
                stack.append(int(i))
        print(stack[0])
        return stack[0]