class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def recurse(i, cur, cursum):
            if cursum == target:
                res.append(cur[:])
                return
            if i >= len(candidates) or cursum > target:
                return
            
            cur.append(candidates[i])
            recurse(i, cur, cursum+candidates[i])
            cur.pop()
            recurse(i+1, cur, cursum)
            return
        recurse(0,[],0)
        return res