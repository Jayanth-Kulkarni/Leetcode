class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        if nums == []:
            return [[]]
        def recurse(i,cur):
            if i >= len(nums):
                res.append(cur[:])
                return
            
            cur.append(nums[i])
            recurse(i+1, cur)
            cur.pop()
            recurse(i+1, cur)

            return
        recurse(0,[])
        return res