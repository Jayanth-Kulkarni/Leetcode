from typing import List

class Solution:
    def recurse(self, candidates, target, ind, current, result):
        if sum(current) == target:
            result.append(current[:])

        for index in range(ind, len(candidates)):
            if (index > ind) and (candidates[index] == candidates[index-1]):
                continue
            if sum(current) + candidates[index] > target:
                break
            current.append(candidates[index])
            self.recurse(candidates, target, index+1, current, result)
            current.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        index = 0
        current = []
        result = []
        candidates = sorted(candidates)
        self.recurse(candidates, target, index, current, result)
        return result
