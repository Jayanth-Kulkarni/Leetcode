class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = defaultdict(int)
        for idx,num in enumerate(nums):
            if target-num in complement:
                return [idx,complement[target-num]]
            complement[num] = idx
