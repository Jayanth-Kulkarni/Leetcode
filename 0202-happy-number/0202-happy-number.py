class Solution:
    def isHappy(self, n: int) -> bool:
        def solve(num):
            new_num = 0
            while num:
                last_digit = num % 10
                num = num // 10
                new_num += last_digit * last_digit
            return new_num
        slow, fast = solve(n), solve(solve(n))
        while slow != fast:
            slow, fast = solve(slow), solve(solve(fast))
            if slow == 1 or fast == 1:
                return True
        if slow == 1 or fast == 1:
            return True
        return False