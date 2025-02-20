class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            first = nums[i]
            l = i+1
            r = len(nums)-1
            while l < r < len(nums):
                second = nums[l]
                third = nums[r]
                if first + second + third == 0:
                    res.append([first, second, third])
                    l += 1
                    while 0 <= l < r < len(nums) and nums[l-1] == nums[l]:
                        l += 1
                
                elif first + second + third > 0:
                    r -= 1
                
                else:
                    l += 1
        return res