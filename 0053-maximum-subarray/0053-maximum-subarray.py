class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = nums[0]
        res = nums[0]
        for i in nums[1:]:
            if cursum < 0:
                cursum = 0
            cursum += i
            res = max(res, cursum)
        return res