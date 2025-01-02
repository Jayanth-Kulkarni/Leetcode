class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, column = len(mat), len(mat[0])
        queue = deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(row):
            for j in range(column):
                if mat[i][j] == 0:
                    queue.append([i,j])
                else:
                    mat[i][j] = float("inf")
        
        while len(queue) > 0:
            r, c =  queue.popleft()
            for i, j in directions:
                new_r, new_c =  r+i, c+j
                if 0<= new_r < row and 0<= new_c < column and mat[new_r][new_c] > mat[r][c] + 1:
                    mat[new_r][new_c] = mat[r][c] + 1
                    queue.append([new_r, new_c])

        return mat