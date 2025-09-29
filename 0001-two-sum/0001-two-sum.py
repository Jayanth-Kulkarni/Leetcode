class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = defaultdict(int)
        for idx, num in enumerate(nums):
            if num in res and num == target-num:
                return [idx, res[target-num]]
            res[num] = idx
            if target - num in res and res[num] != res[target-num]:
                return [idx, res[target-num]]