class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        [4,3,2,2]
        [4,3,2]
        """
        result = 0
        nums.sort(reverse=True)
        for i in range(len(nums)):
            current = nums[i]
            left, right = i+1, len(nums)-1
            while left < right:
                if nums[right] + nums[left] > current:
                    result += (right - left)
                    left += 1
                else:
                    right -= 1
        return result