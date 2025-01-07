class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        queue = deque()
        row, col = len(mat), len(mat[0])
        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    queue.append([r,c])
                else:
                    mat[r][c] = float("inf")
        while len(queue) > 0:
            r, c = queue.popleft()
            for dir in directions:
                n_r, n_c = r + dir[0], c + dir[1]
                if 0 <= n_r < row and 0 <= n_c < col and mat[n_r][n_c] > mat[r][c] + 1:
                    mat[n_r][n_c] =   mat[r][c] + 1
                    queue.append([n_r, n_c])
        return mat