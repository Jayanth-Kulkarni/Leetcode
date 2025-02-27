class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [1] * n
        for i in range(0, m-1, 1):
            newres = [1] * n
            for j in range(n-2,-1,-1):
                newres[j] = newres[j+1] + res[j]
            res = newres
        return res[0]