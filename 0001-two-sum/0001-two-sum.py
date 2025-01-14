class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliment = {}
        for idx, i in enumerate(nums):
            if target-i in compliment:
                return [idx, compliment[target-i]]
            compliment[i] = idx