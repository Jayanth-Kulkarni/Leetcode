class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, cur, sum):
            if i >= len(candidates) or sum > target:
                return
            if sum == target:
                res.append(cur[:])
                return
            cur.append(candidates[i])
            dfs(i, cur, sum+candidates[i])
            cur.remove(candidates[i])
            dfs(i+1, cur, sum)
    
        dfs(0, [], 0)
        return res