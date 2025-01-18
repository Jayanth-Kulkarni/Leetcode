class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # Perform BFS, collect all the cells that are marked 0, mark other cells inf
        row, col = len(mat), len(mat[0])
        queue = deque()
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    queue.append((i,j)) 
                else:
                    mat[i][j] = float("inf")
        
        while len(queue) > 0:
            r, c = queue.popleft()
            for r_, c_ in directions:
                nr, nc = r + r_, c + c_
                if 0 <= nr < row and 0 <= nc < col and mat[nr][nc] > mat[r][c] + 1:
                    mat[nr][nc] = mat[r][c] + 1
                    queue.append((nr, nc))
        
        return mat