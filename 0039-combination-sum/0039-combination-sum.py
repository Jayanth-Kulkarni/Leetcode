class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def recurse(i, cur, sum):
            if sum == target:
                res.append(cur[:])
                return
            if i == len(candidates) or sum > target:
                return
            
            cur.append(candidates[i])
            recurse(i, cur, sum+candidates[i])
            cur.remove(candidates[i])
            recurse(i+1, cur, sum)
        
        recurse(0, [], 0)
        return res