class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        for idx, num in enumerate(nums):
            if target - num in comp:
                return [idx, comp[target-num]]
            comp[num] = idx
        return -1