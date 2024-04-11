def binary_search(nums, target):
    left,right = 0,len(nums)-1
    while left<=right:
        mid = (left+right)//2
        print(left,right,mid,target,nums[mid])
        if nums[mid]==target:
            return mid
        elif nums[mid] > target:
            right = mid-1
        else:
            left = mid+1
    return -1


print(binary_search([1,6,8,10],1))
print(binary_search([11,22,33,44,55,66,77],33))
print(binary_search([-3,-1,0,11,15],0))
print(binary_search([-30,-27,-8,-6,-1],-1))
print(binary_search([0],0))
