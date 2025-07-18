class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preprod, postprod = [nums[0]], [nums[::-1][0]]
        res = []
        for num in nums[1:]:
            preprod.append(preprod[-1] * num)
        nums = nums[::-1]
        for num in nums[1:]:
            postprod.append(postprod[-1] * num)
        postprod = postprod[::-1]
        for i in range(len(preprod)):
            if 0 <= i-1 < i+1 < len(preprod):
                res.append(preprod[i-1] * postprod[i+1])
            elif i-1 < 0:
                res.append(postprod[i+1])
            else:
                res.append(preprod[i-1])
        return res