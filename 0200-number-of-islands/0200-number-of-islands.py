class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited = set()
        r, c = len(grid), len(grid[0])
        island = 0

        def bfs(ro, co):
            queue = deque()
            queue.append((ro, co))
            visited.add((ro,co))

            while len(queue) > 0:
                row, col = queue.popleft()
                for r_, c_ in directions:
                    nr = row + r_
                    nc = col + c_

                    if 0 <= nr < r and 0 <= nc < c and (nr, nc) not in visited and grid[nr][nc] == "1":
                        queue.append((nr,nc))
                        visited.add((nr,nc))


        for row in range(r):
            for col in range(c):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    island += 1
        


        return island