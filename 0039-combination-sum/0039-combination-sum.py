class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        n = len(nums)
        res = []
        cur = []
        def backtrack(i, cur_sum):
            if cur_sum == target:
                res.append(cur[:])
                return
            if cur_sum > target or i == n:
                return
            
            backtrack(i+1, cur_sum)
            cur.append(nums[i])

            backtrack(i, cur_sum + cur[-1])
            cur.pop()

        backtrack(0, 0)
        return res