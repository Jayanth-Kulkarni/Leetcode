class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def recurse(i, cur, sum):
            if i >= len(candidates) or sum > target:
                return
            if sum == target:
                res.append(cur[:])
                return
            
            cur.append(candidates[i])
            recurse(i, cur, sum + candidates[i])
            cur.pop()
            recurse(i+1, cur, sum)

            return
        recurse(0,[],0)
        return res