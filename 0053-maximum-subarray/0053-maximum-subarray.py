class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_array = nums[0]
        cur_sum = 0
        for num in nums:
            if cur_sum <0:
                cur_sum = 0
            cur_sum += num
            max_array = max(max_array,cur_sum)
            print(max_array)
        return max_array
                    