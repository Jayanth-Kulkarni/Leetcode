class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()
        row = len(mat)
        col = len(mat[0])
        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = float("inf")
        
        while len(queue) > 0:
            r, c = queue.popleft()
            for r_, c_ in directions:
                nr, nc = r + r_, c + c_
                if 0 <= nr < row and 0 <= nc < col and mat[nr][nc] > 1 + mat[r][c]:
                    mat[nr][nc] = 1 + mat[r][c]
                    queue.append((nr, nc))
        return mat