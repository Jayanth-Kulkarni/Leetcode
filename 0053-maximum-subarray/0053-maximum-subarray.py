class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l,r = 0,0
        max_sum, cur_sum = nums[0], nums[0]
        r+=1
        while l<r<len(nums):
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += nums[r]
            max_sum = max(max_sum, cur_sum)
            r += 1
        return max_sum