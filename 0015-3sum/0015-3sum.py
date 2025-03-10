class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            if i >0 and nums[i-1] == nums[i]:
                continue
            l = i + 1
            r = len(nums)-1
            while 0 <= l < r:
                f, s, t = nums[i], nums[l], nums[r]
                if f + s + t == 0:
                    res.append([f, s, t])
                    l += 1
                    while 0 <= l <= r and nums[l] == nums[l-1]:
                        l+= 1
                elif f + s + t > 0:
                    r -= 1
                else:
                    l += 1
        return res