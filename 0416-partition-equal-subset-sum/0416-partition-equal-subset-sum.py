class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        
        target = sum(nums)/2
        d = set()
        d.add(0)

        for i in nums:
            copy = set()
            for j in d:
                copy.add(j)
                copy.add(i+j)
            d = copy
            if target in d:
                return True
        
        return False