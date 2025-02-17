class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preprod = [nums[0]]
        postprod = [nums[-1]]

        for i in nums[1:]:
            preprod.append(preprod[-1] * i)

        nums = nums[::-1]
        for i in nums[1:]:
            postprod.append(postprod[-1] * i)
        
        postprod, nums = postprod[::-1], nums[::-1]
        res = []
        for i in range(len(preprod)):
            if i > 0 and i < len(preprod)-1:
                res.append(preprod[i-1] * postprod[i+1])
            elif i > 0:
                res.append(preprod[i-1])
            elif i < len(preprod):
                res.append(postprod[i+1])
        
        return res