class Solution:
    def isHappy(self, n: int) -> bool:
        def findHappy(n):
            res = 0
            while n:
                res += (n % 10) * (n % 10)
                n = n // 10
            return res
        
        slow, fast = findHappy(n), findHappy(findHappy(n))
        while fast != slow:
            slow, fast = findHappy(slow), findHappy(findHappy(fast))
            if slow == 1 or fast == 1:
                return True
        return slow == 1