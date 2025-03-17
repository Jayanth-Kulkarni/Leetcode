class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [1] * n
        for i in range(m-1, 0, -1):
            new_res = [1] * n 
            for j in range(n - 2, -1, -1):
                new_res[j] = res[j] + new_res[j+1]
            res = new_res
        return res[0]