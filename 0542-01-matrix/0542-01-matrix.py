class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        q = deque()
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = float("inf")
        
        while q:
            r1, c1 = q.popleft()
            for r_, c_ in [(1,0), (-1,0), (0,1), (0,-1)]:
                r = r1 + r_
                c = c1 + c_
                if 0 <= r < row and 0 <= c < col and mat[r][c] > 1 + mat[r1][c1]:
                    mat[r][c] = 1 + mat[r1][c1]
                    q.append((r,c))
        
        return mat