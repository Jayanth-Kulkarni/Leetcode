class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        carry = 0
        res = []
        for i in range(max(len(a), len(b))):
            digita = int(a[i]) if i < len(a) else 0
            digitb = int(b[i]) if i < len(b) else 0
            sum = digita + digitb + carry
            res.append(str(sum%2))
            carry = int(sum/2)
        
        if carry:
            res.append("1")
        
        return "".join(res[::-1])