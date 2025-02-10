class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        queue = deque()
        for r in range(row):
            for c in range(col):
                if mat[r][c] == 1:
                    mat[r][c] = float("inf")
                else:
                    queue.append((r,c))
        
        while len(queue) > 0:
            ro, co = queue.popleft()
            for r_, c_ in [(1,0), (-1,0), (0,1), (0,-1)]:
                r = ro + r_
                c = co + c_
                if 0 <= r < row and 0 <= c < col and mat[r][c] > mat[ro][co] + 1:
                    mat[r][c] = mat[ro][co] + 1
                    queue.append((r,c))
        
        return mat