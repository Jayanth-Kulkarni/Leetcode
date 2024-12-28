class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = defaultdict(int)
        for idx,num in enumerate(nums):
            if target-num in result:
                return [idx,result[target-num]]
            result[num] = idx