class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        dp = set()
        dp.add(0)
        target = sum(nums)/2
        for num in nums:
            copy = set()
            for i in dp:
                copy.add(i + num)
                copy.add(i)
                if target in dp:
                    return True
            dp = copy
        return False