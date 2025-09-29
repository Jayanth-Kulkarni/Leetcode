class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preprocess, postprocess = [nums[0]], [nums[-1]]
        for num in nums[1:]:
            preprocess.append(preprocess[-1] * num)
        nums = nums[::-1]
        for num in nums[1:]:
            postprocess.append(postprocess[-1] * num)
        postprocess = postprocess[::-1]
        print(preprocess, postprocess)
        res = []
        for idx, i in enumerate(preprocess):
            if idx-1<0:
                res.append(postprocess[idx+1])
            elif idx+1 > len(nums)-1:
                res.append(preprocess[idx-1])
            else:
                res.append(postprocess[idx+1] * preprocess[idx-1])
        print(res)
        return res