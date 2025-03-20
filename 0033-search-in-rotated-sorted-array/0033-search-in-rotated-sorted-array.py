class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            # mid is in the left
            if nums[l] <= nums[mid]:
                if target < nums[l] or nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
            # mid is in the right
            else:
                if nums[r] < target or nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
        return -1