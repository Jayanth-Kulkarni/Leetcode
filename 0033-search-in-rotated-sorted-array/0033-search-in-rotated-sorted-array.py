class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            # mid is in the left sorted array
            if nums[l] <= nums[m]:
                if target < nums[l] or nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
            # mid is in the right sorted array
            else:
                if target > nums[r] or nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l  = m + 1
        return -1 
