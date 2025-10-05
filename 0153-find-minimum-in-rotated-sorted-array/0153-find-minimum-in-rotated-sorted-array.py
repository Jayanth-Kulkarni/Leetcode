class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        res = nums[0]
        r = len(nums)-1
        left_val,right_val = nums[l],nums[r]
        while l<=r:
            if nums[l]<nums[r]:
                res = min(res,nums[l])
                break
            mid = int((l+r)/2)
            res = min(res,nums[mid])
            if nums[mid] >= left_val:
                l = mid+1
            else:
                r = mid-1
        return res