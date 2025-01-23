class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            f = nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r < len(nums):
                s, t = nums[l], nums[r]
                if f + s + t == 0:
                    result.append([f, s, t])
                    l += 1
                    while 0 < l < r and nums[l-1] == nums[l]:
                        l += 1
                elif f + s + t > 0:
                    r -= 1
                else:
                    l += 1
        return result