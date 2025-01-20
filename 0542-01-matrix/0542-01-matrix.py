class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        queue = deque()
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = float("inf")
        
        while len(queue) > 0:
            r, c = queue.popleft()
            for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                n_r = dir[0] + r
                n_c = dir[1] + c
                if 0 <= n_r < row and 0 <= n_c < col and mat[n_r][n_c] > 1 + mat[r][c]:
                    mat[n_r][n_c] = 1 + mat[r][c]
                    queue.append((n_r, n_c))
        
        return mat