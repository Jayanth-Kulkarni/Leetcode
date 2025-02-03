class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        carry = 0
        res = []
        
        for i in range(max(len(a), len(b))):
            digit_a = int(a[i]) if i < len(a) else 0
            digit_b = int(b[i]) if i < len(b) else 0
            
            total = digit_a + digit_b + carry
            res.append(str(total % 2))
            carry = total // 2
        
        if carry:
            res.append('1')
        
        return ''.join(res[::-1])
