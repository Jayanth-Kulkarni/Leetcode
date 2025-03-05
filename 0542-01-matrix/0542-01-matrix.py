class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        q = deque()
        for r in range(row):
            for c in range(col):
                if mat[r][c] == 1:
                    mat[r][c] = float("inf")
                else:
                    q.append((r,c))
        
        while q:
            r1,c1 = q.popleft()
            for i, j in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                r,c = r1+i, c1+j
                if 0 <= r < row and 0 <= c < col and mat[r][c] > mat[r1][c1] + 1:
                    mat[r][c] = mat[r1][c1] + 1
                    q.append((r,c))
        
        return mat
