class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        q = deque()
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 1:
                    mat[i][j] = float("inf")
                else:
                    q.append((i, j))
        
        while q:
            r,c = q.popleft()
            for i,j in [(1,0), (-1,0), (0, 1), (0, -1)]:
                nr, nc= r+i, c+j
                if 0 <= nr < row and 0 <= nc < col and mat[nr][nc] > 1 + mat[r][c]:
                    mat[nr][nc] = 1 + mat[r][c] 
                    q.append((nr,nc))
        
        return mat