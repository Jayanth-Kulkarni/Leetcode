class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = collections.defaultdict(int)
        for idx,i in enumerate(nums):
            difference = target - i
            if i in numbers:
                return [idx,numbers[i]]
            numbers[difference] = idx
        return []