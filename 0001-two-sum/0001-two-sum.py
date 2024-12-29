class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = defaultdict(int)
        for idx,num in enumerate(nums):
            diff = target-num
            if diff in mem:
                return [mem[target-num],idx]
            mem[num] = idx