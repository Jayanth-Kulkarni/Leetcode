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
                if first + nums[l] + nums[r] == 0:
                    res.append([first, nums[l], nums[r]])
                    l+=1
                    while l < r < len(nums) and nums[l-1] == nums[l]:
                        l+=1
                elif l < r < len(nums) and first + nums[l] + nums[r] > 0:
                    r -= 1
                elif l < r < len(nums):
                    l += 1
            
        return res