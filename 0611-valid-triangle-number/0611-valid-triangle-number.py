class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for last in range(len(nums)-1, -1, -1):
            biggest = nums[last]
            l, r = 0, last-1
            while l < r:
                if nums[l] + nums[r] > biggest:
                    res += r-l
                    r -= 1
                else:
                    l += 1
        return res