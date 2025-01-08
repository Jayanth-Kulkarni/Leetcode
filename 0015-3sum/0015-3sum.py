class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        i = 0
        result = []
        while i < len(nums):
            while 0 < i < len(nums)-1 and nums[i-1] == nums[i]:
                i += 1
            first = nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                ts = first + nums[l] + nums[r]
                if ts == 0:
                    result.append([first, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                elif ts > 0:
                    r -= 1
                else:
                    l += 1
            i += 1
        return result
