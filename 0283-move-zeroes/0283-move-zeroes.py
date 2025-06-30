class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        next_insert_pos = 0
        for current in range(len(nums)):
            if nums[current] != 0:
                nums[current], nums[next_insert_pos] = nums[next_insert_pos], nums[current]
                next_insert_pos += 1
            