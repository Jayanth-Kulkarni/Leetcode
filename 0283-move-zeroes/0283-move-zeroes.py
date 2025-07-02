class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        next_swap_position = 0
        for current_position in range(len(nums)):
            if nums[current_position] != 0:
                nums[current_position],  nums[next_swap_position] =  nums[next_swap_position],  nums[current_position]
                next_swap_position += 1