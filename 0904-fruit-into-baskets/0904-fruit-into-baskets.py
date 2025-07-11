class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res_dict = defaultdict(int)
        l = r = res = max_res = 0
        while l <= r < len(fruits):
            res_dict[fruits[r]] += 1
            res += 1
            while l <= r < len(fruits) and len(res_dict) > 2:
                res_dict[fruits[l]] -= 1
                res -= 1
                if res_dict[fruits[l]] == 0:
                    del res_dict[fruits[l]]
                l+=1
            r+=1
            max_res = max(res,max_res)
        return max_res