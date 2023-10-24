from collections import Counter

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
d = {}
for idx, str in enumerate(strs):
    sorted = list(str)
    sorted.sort()
    s = "".join(sorted)
    if s not in d:
        d[s] = []
    d[s].append(str)

res = []
for value in d.values():
    res.append(value)

print(res)