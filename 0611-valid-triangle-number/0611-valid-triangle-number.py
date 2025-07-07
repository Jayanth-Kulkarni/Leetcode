class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        1. Sort them
        2. Have the last pointer to the end
        3. 
        """

        nums.sort()
        count = 0
        for current_biggest in range(len(nums)-1, -1, -1):
            l, r = 0, current_biggest - 1
            while l < r:
                if nums[l] + nums[r] > nums[current_biggest]:
                    count +=  r - l
                    r -= 1
                else:
                    l += 1
        return count