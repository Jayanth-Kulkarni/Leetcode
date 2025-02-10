class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        res = ""
        carry = 0
        for i in range(max(len(a), len(b))):
            digita = int(a[i]) if i < len(a) else 0
            digitb = int(b[i]) if i < len(b) else 0

            sum = (digita + digitb + carry) % 2
            carry = int((digita + digitb + carry) / 2)

            res += str(sum)
        
        if carry:
            res += "1"
        
        return res[::-1]
