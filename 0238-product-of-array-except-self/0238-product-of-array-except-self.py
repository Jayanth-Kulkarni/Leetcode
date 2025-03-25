class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preprod, postprod = [nums[0]], [nums[-1]]
        for i in nums[1:]:
            preprod.append(preprod[-1] * i)
        nums = nums[::-1]
        for i in nums[1:]:
            postprod.append(postprod[-1] * i)
        postprod = postprod[::-1]
        res = []
        for i in range(len(nums)):
            if i-1 >= 0 and i + 1 < len(nums):
                res.append(preprod[i-1] * postprod[i+1])
            elif i-1 < 0:
                res.append(postprod[i+1])
            elif i+1 >= len(nums):
                res.append(preprod[i-1])
        return res