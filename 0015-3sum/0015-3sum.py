class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            first = nums[i]
            l = i + 1
            r = len(nums) - 1
            while l<r:
                if first + nums[l] + nums[r] == 0:
                    result.append([first, nums[l], nums[r]])
                    l += 1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
                elif first + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
            i+=1
        return result