class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [a,b,c,d]
        # [a,ab,abc,abcd]
        # [abcd,bcd,cd,d]
        # [bcd,acd,abd,abc]

        preprod = [nums[0]]
        for num in nums[1:]:
            preprod.append(preprod[-1] * num)
        
        postprod = [nums[-1]]
        rev = nums[::-1]
        for num in rev[1:]:
            postprod.append(postprod[-1] * num)
        
        postprod = postprod[::-1]

        res = []
        for i in range(len(preprod)):
            if 0 <= i-1 < len(preprod) and 0 <= i+1 < len(preprod):
                res.append(preprod[i-1] * postprod[i+1])
            elif 0 <= i-1 < len(preprod):
                res.append(preprod[i-1])
            elif 0 <= i+1 < len(preprod):
                res.append(postprod[i+1])
        return res