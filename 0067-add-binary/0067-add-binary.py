class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        num = 0
        carry = 0
        res = []
        for i in range(max(len(a),len(b))):
            num1 = int(a[i]) if i < len(a) else 0
            num2 = int(b[i]) if i < len(b) else 0
            sum = (num1 + num2 + carry) %2
            carry = int((num1 + num2 + carry) / 2)
            res.append(str(sum))
        if carry:
            res.append(str(carry))
        
        res = "".join(res)
        res = res[::-1]
        return res