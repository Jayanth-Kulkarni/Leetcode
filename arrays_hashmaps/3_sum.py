class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        for idx, num in enumerate(nums):
            if idx>0 and num==nums[idx-1]:
                continue
            target = 0 - num
            start,end = idx+1, len(nums)-1
            while start<end:
                if nums[start]+nums[end]==target:
                    result.append([nums[start],nums[end],-target])
                    start+=1
                    end-=1
                    while nums[start] == nums [start-1] and start<end:
                        start+=1
                    while nums[end] == nums [end+1] and start<end:
                        end-=1
                elif nums[start]+nums[end]>target:
                    end -= 1
                else:
                    start+=1
            prev_num = num
        return result