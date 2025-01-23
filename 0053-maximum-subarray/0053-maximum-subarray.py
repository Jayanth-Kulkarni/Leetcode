class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val, cur_max = nums[0], nums[0]
        for num in nums[1:]:
            if cur_max <0:
                cur_max = 0
            cur_max += num
            max_val = max(cur_max, max_val)
        return max_val