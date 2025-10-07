class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        current = []
        def dfs(i, cur_sum):
            if i >= len(candidates) or cur_sum >= target:
                if cur_sum == target:
                    res.append(current.copy())
                return
            current.append(candidates[i])
            dfs(i, sum(current))
            current.pop()
            dfs(i+1, sum(current))
        dfs(0,0)
        return res