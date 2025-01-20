class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_prod = [nums[0]]
        for i in nums[1:]:
            pre_prod.append(i * pre_prod[-1])
        
        reverse = nums[::-1]
        post_prod = [reverse[0]]
        for i in reverse[1:]:
            post_prod.append(i * post_prod[-1])
        
        res = []

        # [a, b, c, d]
        # pre_prod = [a, ab, abc, abcd]
        # post_prod = [abcd, dcb, dc, d]
        # res = [dcb, adc, abd, abc]
        post_prod = post_prod[::-1]
        for i in range(len(nums)):
            if i-1 >=0 and i+1 < len(nums):
                res.append(pre_prod[i-1] * post_prod[i+1])
            elif  i-1 >= 0:
                res.append(pre_prod[i-1])
            elif  i+1 < len(nums):
                res.append(post_prod[i+1])
        
        return res