# nums = [-1,0,1,2,-1,-4]
nums = [0, 0, 0, 0]
ans = [[-1,-1,2],[-1,0,1]]
nums = sorted(nums)
print(nums)
res = []
for ida,num in enumerate(nums):
    if ida>0 and num==nums[ida-1]:
        continue
    left,right = ida+1,len(nums)-1
    while left<right:
        threesum = num+nums[left]+nums[right]
        if threesum<0:
            left+=1
        elif threesum>0:
            right-=1
        else:
            res.append([num,nums[left],nums[right]])
            while nums[left] == nums[left-1] and left<right:
                left +=1
print(res)