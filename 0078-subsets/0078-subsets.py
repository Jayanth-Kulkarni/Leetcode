class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        def recurse(cur, i):
            if i >= len(nums):
                res.append(cur[:])
                return
            cur.append(nums[i])
            recurse(cur, i+1)
            cur.pop()
            recurse(cur, i+1)
        recurse([], 0)
        return res