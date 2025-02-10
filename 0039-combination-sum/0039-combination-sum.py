class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(curSum, cur, i):
            if curSum == target:
                res.append(cur[:])
                return

            if i >= len(candidates) or curSum > target:
                return
            
            cur.append(candidates[i])
            dfs(curSum + candidates[i], cur, i)
            cur.pop()
            dfs(curSum, cur, i+1)
            
            return 

        dfs(0, [], 0)
        return res