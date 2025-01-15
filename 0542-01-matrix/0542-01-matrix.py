class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        r, c = len(mat), len(mat[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        # Refill the non-zero cells to be inf

        queue = deque()
        for row in range(r):
            for col in range(c):
                if mat[row][col] == 0:
                    queue.append((row,col))
                else:
                    mat[row][col] = float("inf")
        # Loop through the queue and perform DFS and update the values
        
        while len(queue) > 0:
            r, c = queue.popleft()
            for nr, nc in directions:
                new_r, new_c = r+nr, c+nc
                if 0 <= new_r < len(mat) and 0 <= new_c < len(mat[0]) and mat[new_r][new_c] > mat[r][c] + 1:
                    mat[new_r][new_c] = mat[r][c] + 1
                    queue.append((new_r, new_c))
        
        return mat