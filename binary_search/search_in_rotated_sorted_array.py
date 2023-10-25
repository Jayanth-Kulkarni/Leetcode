class Solution:
    def findMin(self, nums) -> int:
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


if __name__ == "__main__":
    solve = Solution()
    print(solve.findMin(nums=[3,4,5,6,0,1,2]))