class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        for i in range(len(nums)):
            if i>0 and nums[i-1] == nums[i]:
                continue
            f = nums[i]
            l, r = i+1, len(nums)-1
            while l < r < len(nums):
                s, t = nums[l], nums[r]
                if f + s + t == 0:
                    result.append([f, s, t])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif l < r < len(nums) and f + s + t > 0:
                    r -= 1
                elif l < r < len(nums) and f + s + t < 0:
                    l += 1
        return result
                    

