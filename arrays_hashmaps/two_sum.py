nums = [-1, -2, -3, -4, -5]
target = -8

d = {}
for idx, num in enumerate(nums):
    if num not in d:
        d[num] = []
    d[num].append(idx)

print(d)
for num in nums:
    if target - num in d:
        if d[num] == d[target - num] and len(d[num]) == 1:
            continue
        elif d[num] == d[target - num] and len(d[num]) > 1:
            print(d[num])
        else:
            print(d[num][0], d[target - num][0])
