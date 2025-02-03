class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        carry = 0
        res = []

        for i in range(max(len(a), len(b))):
            digit1 = int(a[i]) if i < len(a) else 0
            digit2 = int(b[i]) if i < len(b) else 0
            
            sum = (digit1 + digit2 + carry) % 2
            carry = (digit1 + digit2 + carry) // 2
            res.append(str(sum))
        
        if carry:
            res.append("1")
        
        return "".join(res[::-1])