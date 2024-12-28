class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_array = {}
        for idx,num in enumerate(nums):
            target_array[num] = idx
        for idx,num in enumerate(nums):
            if target-num in target_array and target_array[target-num] <= idx:
                continue
            elif target-num in target_array:
                return [idx,target_array[target-num]]