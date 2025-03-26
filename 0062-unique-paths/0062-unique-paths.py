class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [1] * n
        for i in range(m-1, 0, -1):
            newres = [1] * n
            for j in range(n-2, -1, -1):
                newres[j] = res[j] + newres[j+1]
            res = newres
        return res[0]