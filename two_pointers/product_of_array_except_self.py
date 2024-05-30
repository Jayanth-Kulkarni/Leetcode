def product_except_self(arr):
    left,right = 0,len(arr)-1
    prefix_product,postfix_product=[],[]
    prefix,postfix=1,1
    while left<=len(arr)-1 and right>=0:
        prefix *= arr[left]
        postfix *= arr[right]
        prefix_product.append(prefix)
        postfix_product.append(postfix)
        left+=1
        right-=1
    postfix_product = postfix_product[::-1]
    prefix_product.insert(0,1)
    postfix_product.insert(len(postfix_product),1)
    result = []
    for idx,i in enumerate(arr):
        result.append(prefix_product[idx]*postfix_product[idx+1])
    return result

# Solution below does not include 2 pointers, I have 2 different passes of forward and reverse of the array
def productExceptSelf2(self, nums: List[int]) -> List[int]:
    prefix_mul = [1]
    postfix_mul = [1]
    result = []
    for idx,i in enumerate(nums):
        prefix_mul.append(prefix_mul[idx]*nums[idx])
    rev_nums = nums[::-1]
    for idx,i in enumerate(rev_nums):
        postfix_mul.append(postfix_mul[idx]*rev_nums[idx])
    postfix_mul = postfix_mul[::-1]
    print(prefix_mul,postfix_mul)
    for i,j in zip(prefix_mul[0:-1],postfix_mul[1:]):
        result.append(i*j)
    return result
    # 0 to n-2
    # 1 to n-1

# pre-multiplication = [1]+[1,2,6,24]
# post-multiplication = [24,24,12,4]+[1]
# result = [24,12,8,6]

product_except_self([3,-1,-3,2,1,-2])