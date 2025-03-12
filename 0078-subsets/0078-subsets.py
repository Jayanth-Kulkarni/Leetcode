class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def recurse(i, cur):
            if i == len(nums):
                res.append(cur[:])
                return
            cur.append(nums[i])
            recurse(i+1, cur)
            cur.remove(nums[i])
            recurse(i+1, cur)
        recurse(0, [])
        return res