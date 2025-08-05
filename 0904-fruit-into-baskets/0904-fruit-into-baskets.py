class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = defaultdict(int)
        max_len = l =  0
        for r in range(len(fruits)):
            res[fruits[r]] += 1
            while len(res) > 2:
                res[fruits[l]] -= 1
                if res[fruits[l]] == 0:
                    del res[fruits[l]]
                l += 1
            max_len = max(max_len, r-l+1)
        return max_len