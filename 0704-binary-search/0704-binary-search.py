class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r,mid=0,len(nums)-1,(len(nums)-1)//2
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        return -1
            
