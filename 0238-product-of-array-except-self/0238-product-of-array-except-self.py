class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        
        # preprod
        preprod = [nums[0]]
        for idx, i in enumerate(nums[1:]):
            preprod.append(preprod[-1] * i)
        
        rev = nums[::-1]
        print(rev)
        postprod = [rev[0]]
        for idx, i in enumerate(rev[1:]):
            postprod.append(postprod[-1] * i)
        
        postprod = postprod[::-1]

        print(preprod,postprod)
        for i in range(len(nums)):
            if i-1>=0 and i+1<len(nums):
                result.append(preprod[i-1] * postprod[i+1])
            elif i-1>=0: 
                result.append(preprod[i-1])
            elif i+1<len(nums):
                result.append(postprod[i+1])
        return result