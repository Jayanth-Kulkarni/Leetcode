class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for cur in range(len(nums)-1, -1, -1):
            l, r = 0, cur-1
            while l < r:
                if nums[l] + nums[r] > nums[cur]:
                    res += (r - l)
                    r -= 1
                else:
                    l += 1
        return res