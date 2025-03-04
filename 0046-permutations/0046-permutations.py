class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        perms = self.permute(nums[1:])
        res = []
        
        for num in perms:
            for i in range(len(num)+1):
                copy = num.copy()
                copy.insert(i, nums[0])
                res.append(copy)
        
        return res