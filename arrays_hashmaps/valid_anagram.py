from collections import Counter

s = "anagram"
t = "nagram"

print(Counter(list(s)) == Counter(list(t)))
