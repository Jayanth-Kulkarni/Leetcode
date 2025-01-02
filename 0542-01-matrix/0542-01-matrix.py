class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        move = [(0,1),(0,-1),(1,0),(-1,0)]
        queue = deque()
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    queue.append([i,j])
                else:
                    mat[i][j] = float("inf")

        while len(queue) > 0:
            i, j = queue.popleft()
            for dir_i, dir_j in move:
                new_i, new_j = i + dir_i, j +  dir_j
                if 0 <= new_i < row and 0 <= new_j < col and mat[new_i][new_j] > mat[i][j] + 1:
                    mat[new_i][new_j] = mat[i][j] + 1
                    queue.append([new_i,new_j])

        return mat