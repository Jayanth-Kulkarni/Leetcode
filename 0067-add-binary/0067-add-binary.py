class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a,b = a[::-1], b[::-1]
        res = []
        carry = 0
        for i in range(max(len(a), len(b))):
            n1 = int(a[i]) if i < len(a) else 0
            n2 = int(b[i]) if i < len(b) else 0
            sum = (n1 + n2 + carry)
            carry = int(sum / 2)
            sum = sum % 2
            res.append(str(sum))
        if carry:
            res.append(str(carry))
        res = res[::-1]
        return "".join(res)