class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        nums = [2,3,4,4]
        first_pointer = 4
        second_pointer = 2
        third_pointer = 4
        """
        nums.sort()
        res = 0
        for high in range(len(nums)-1, -1, -1):
            left, right = 0, high-1
            while left < right:
                if nums[left] + nums[right] > nums[high]:
                    res += right - left
                    right -= 1
                else:
                    left += 1
        return res
        