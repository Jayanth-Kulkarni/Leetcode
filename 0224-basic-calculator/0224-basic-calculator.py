class Solution:
    def calculate(self, s: str) -> int:
        # Initialize variables
        result = 0          # Keeps track of current result
        current_num = 0     # Builds the current number
        sign = 1           # Current sign (1 for +, -1 for -)
        stack = []         # Stack for handling parentheses

        for char in s:
            # If character is a digit, build the number
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            
            # If character is + or -
            elif char in "+-":
                # Add previous number to result
                result += current_num * sign
                current_num = 0
                # Update sign for next number
                sign = 1 if char == "+" else -1
            
            # If opening parenthesis
            elif char == "(":
                # Save current state
                stack.append(result)
                stack.append(sign)
                # Reset for new calculation
                result = 0
                sign = 1
            
            # If closing parenthesis
            elif char == ")":
                # Add final number inside parentheses
                result += current_num * sign
                # Multiply by previous sign
                result *= stack.pop()
                # Add to previous result
                result += stack.pop()
                current_num = 0

        # Add the last number if exists
        return result + (current_num * sign)