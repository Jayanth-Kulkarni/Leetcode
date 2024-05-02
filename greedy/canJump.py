class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = nums[len(nums)-1]
        for index in range(len(nums)-1,-1,-1):
            if index + nums[index] >= target:
                target = index
        
        return True if target==0 else False

            
