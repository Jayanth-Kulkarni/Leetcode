class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # mark all the 2s to the queue
        queue =  deque()
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i, j))
        iterations = 0
        visited = set()
        while len(queue) > 0:
            for i in range(len(queue)):
                r,c = queue.popleft()
                for dir in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                    n_r = r + dir[0]
                    n_c = c + dir[1]
                    if 0 <= n_r < row and 0 <= n_c < col and grid[n_r][n_c] == 1 and (n_r, n_c) not in visited:
                        grid[n_r][n_c] = 2
                        queue.append((n_r, n_c))
                        visited.add((n_r, n_c))
            if len(queue) > 0:
                iterations += 1
        
        complete = True
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    complete = False

        return iterations if complete else -1