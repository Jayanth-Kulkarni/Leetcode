class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        island = 0
        visited = set()

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            while len(queue) > 0:
                r, c = queue.popleft()
                for ro, co in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + ro, c + co
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == "1" and (nr, nc) not in visited:
                        queue.append((nr, nc))
                        visited.add((nr, nc)) 

                
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    island += 1


        return island