import re

s = "A man, a plan, a canal: Panama"
s = s.lower().replace(" ", "")
s = re.sub(r'\W+', '', s)
return s == s[::-1]


# alternate solution

def is_palindrome(s):
  left = 0
  right = len(s)-1
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