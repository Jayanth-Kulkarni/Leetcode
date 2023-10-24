d = {"{": "}", "[": "]", "(": ")"}
stack = []
for symbol in list(s):
    if symbol in d:
        stack.append(symbol)
    elif len(stack) == 0:
        return False
    elif d[stack[len(stack) - 1]] == symbol:
        stack.pop()
    else:
        return False
return len(stack) == 0
