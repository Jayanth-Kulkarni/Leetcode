import re

s = "A man, a plan, a canal: Panama"
s = s.lower().replace(" ", "")
s = re.sub(r'\W+', '', s)
return s == s[::-1]
