class Solution:
    def search(self, nums, target) -> int:
        l = 0
        res = nums[0]
        r = len(nums)-1
        left_val,right_val = nums[l],nums[r]
        while l<=r:
            if target == nums[l]:
                return l
            elif target == nums[r]:
                return r
            mid = int((l+r)/2)
            # print("outside",mid,r,l,nums[mid],nums)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if nums[l] > nums[r] and target<nums[l]:
                    # print("elif moving left pointer",mid,r,l,nums[mid],nums,target)
                    l = mid+1
                elif nums[l] > nums[r] and target>nums[l]:
                    # print("elif moving right pointer",mid,r,l,nums[mid],nums,target)
                    r = mid-1
                else:
                    r = mid-1
            else:
                l = mid+1   
                # if nums[l] > nums[r] and (target<nums[l] and target<nums[r]):
                #     print("else moving left pointer",mid,r,l,nums[mid],nums,target)
                # else:
                #     print("else moving left pointer",mid,r,l,nums[mid],nums,target)
                #     r = mid-1
        return -1


if __name__ == "__main__":
    solve = Solution()
    print(solve.search(nums=[3,4,5,6,0,1,2],target=0))
    print(solve.search(nums = [4,5,6,7,0,1,2], target = 0))
    print(solve.search(nums = [4,5,6,7,0,1,2], target = 3))
    print(solve.search(nums=[3,5,1],target=3))
    print(solve.search(nums=[4,5,6,7,0,1,2],target=5))
    print(solve.search(nums = [1], target = 0)) 
    print(solve.search(nums=[8,1,2,3,4,5,6,7],target = 6))