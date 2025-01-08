class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, num in enumerate(nums):
            d = target - num
            if d in seen:
                return [seen[d], idx]
            seen[num] = idx