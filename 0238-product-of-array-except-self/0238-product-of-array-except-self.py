class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # calculate preprod, and postprod
        # [a, b, c, d]
        # preprod = [a, ab, abc, abcd]
        # postprod = [abcd, bcd, cd, d]
        # result = [bcd, acd, abd, abc]
        preprod = [nums[0]]
        for num in nums[1:]:
            preprod.append(preprod[-1] * num)
        
        reversed_nums = nums[::-1]
        postprod = [reversed_nums[0]]
        for num in reversed_nums[1:]:
            postprod.append(postprod[-1] * num)

        postprod = postprod[::-1]
        
        result = []

        for i in range(len(nums)):
            if i>0 and i<len(nums)-1:
                result.append(preprod[i-1] * postprod[i+1])
            elif i>0:
                result.append(preprod[i-1])
            elif i<len(nums)-1:
                result.append(postprod[i+1])
        
        return result