class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the numbers, and skip the repeated values for first and second positions
        nums =  sorted(nums)
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            first = nums[i]
            l = i+1 
            r = len(nums)-1
            while l < r < len(nums):
                three_sum = first + nums[l] + nums[r]
                if l < r < len(nums) and three_sum > 0:
                    r -= 1
                elif l < r < len(nums) and three_sum < 0:
                    l += 1
                elif three_sum == 0:
                    result.append([first, nums[l], nums[r]])
                    l += 1
                    while l < r < len(nums) and nums[l-1] == nums[l]: 
                        l += 1
        return result