class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nextnonzero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[nextnonzero] = nums[nextnonzero], nums[i]
                nextnonzero += 1
        return nums