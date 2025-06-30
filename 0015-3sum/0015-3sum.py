class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Sort the nums
        make sure to skip the repeats to avoid duplicates in the list
        """
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while 0 < left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right < len(nums) and nums[right] == nums[right+1]:
                        right -= 1
                elif sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
        return result