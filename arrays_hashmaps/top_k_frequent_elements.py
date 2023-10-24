nums = [1, 1, 1, 2, 2, 3]
k = 2
d = {}
for num in nums:
    if num not in d:
        d[num] = 0
    d[num] += 1

sorted_dict = dict(
    sorted(list(d.items()), key=lambda item: item[1], reverse=True))
print(list(sorted_dict.keys())[:k])
