class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, cur, cursum):
            if cursum == target:
                res.append(cur[:])
                return
            
            if i >= len(candidates) or cursum > target:
                return 

            cur.append(candidates[i])
            dfs(i, cur, cursum + candidates[i])
            cur.pop()
            dfs(i+1, cur, cursum)

            return
        dfs(0,[],0)
        return res