class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        target = sum(nums)/2
        dp = set()
        dp.add(0)
        for num in nums:
            copy = set()
            for ele in dp:
                copy.add(ele+num)
                copy.add(ele)
            dp = copy
            if target in dp:
                return True
        return False
            