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
            r_,c_ = q.popleft()
            for r1,c1 in [(1,0), (-1,0), (0,1), (0,-1)]:
                r = r1+r_
                c = c1+c_
                if 0 <= r < row and 0 <= c < col and mat[r][c] > mat[r_][c_] + 1:
                    mat[r][c] = mat[r_][c_] + 1
                    q.append((r,c))

        return mat