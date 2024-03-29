import re

s = "A man, a plan, a canal: Panama"
s = s.lower().replace(" ", "")
s = re.sub(r'\W+', '', s)
return s == s[::-1]


# alternate solution
def isPalindrome(self, s: str) -> bool:
    s = s.lower().replace(" ","")
    s = re.sub(r'\W|_', '', s)
    print(s)
    if len(s)==0:
        return True
    left = 0
    right = len(s)-1
    print(left,right)
    if s[left]!=s[right]:
        return False
    left +=1
    right -=1
    while left < right:
        print(s[left],s[right])
        if s[left]!=s[right]:
            return False
        left +=1
        right -=1
    return True

