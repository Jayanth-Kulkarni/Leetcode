class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:        
        preprod = [nums[0]]
        postprod = [nums[::-1][0]]
        running_prod = nums[0]
        for i in nums[1:]:
            running_prod = running_prod * i
            preprod.append(running_prod)

        running_prod = nums[::-1][0]
        for i in nums[:-1][::-1]:
            running_prod = running_prod * i
            postprod.append(running_prod)
        
        postprod = postprod[::-1]
        result = []
        for i in range(len(nums)):
            if i-1 >= 0 and i+1 < len(nums):
                result.append(preprod[i-1] * postprod[i+1])
            elif i-1 >= 0:
                result.append(preprod[i-1])
            elif i+1 < len(nums):
                result.append(postprod[i+1])
        
        return result