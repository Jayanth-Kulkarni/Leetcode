class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        dp = set()
        dp.add(0)
        target = sum(nums)/2
        for num in nums:
            copy = set()
            for e in dp:
                copy.add(num + e)
                copy.add(e)
            dp = copy
            if target in dp:
                return True
        return False