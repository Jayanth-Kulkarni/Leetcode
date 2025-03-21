class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums)/2
        d = set()
        d.add(0)
        for num in nums:
            copy = set()
            for i in d:
                copy.add(i)
                copy.add(i+num)
            d = copy
            if target in copy:
                return True

        return False