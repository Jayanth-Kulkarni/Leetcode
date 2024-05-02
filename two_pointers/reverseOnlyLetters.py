class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        start = 0
        end = len(s)-1
        s = list(s)
        while start<=end:
            if s[start].isalpha() and s[end].isalpha():
                s[start],s[end]=s[end],s[start]
                start +=1
                end -=1
            elif s[start].isalpha()!=1:
                start +=1
            elif s[end].isalpha()!=1:
                end -=1
        return "".join(s)