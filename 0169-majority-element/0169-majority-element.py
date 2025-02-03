class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        for ele, count in d.items():
            if count >= len(nums)/2:
                return ele