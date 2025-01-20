class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the nums array
        nums = sorted(nums)
        res = []
        i = 0
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            first = nums[i]
            l, r = i+1, len(nums)-1
            while 0 <= l < r < len(nums):
                if first + nums[l] + nums[r] == 0:
                    res.append([first, nums[l], nums[r]])
                    l += 1
                    while 0 <= l < r < len(nums) and nums[l-1] == nums[l]:
                        l += 1
                elif first + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r-=1
        return res
