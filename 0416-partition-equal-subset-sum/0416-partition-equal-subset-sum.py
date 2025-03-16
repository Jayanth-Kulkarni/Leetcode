class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        target = sum(nums)/2
        d = set()
        d.add(0)
        for i in nums:
            print(d, target)
            c = set()
            for j in d:
                c.add(j)
                c.add(i+j)
            if target in c:
                return True
            d = c
        return False