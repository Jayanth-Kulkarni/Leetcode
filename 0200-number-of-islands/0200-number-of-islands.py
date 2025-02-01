class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        row, col = len(grid), len(grid[0])
        visited = set()

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r,c))
            while len(queue) > 0:
                r_, c_ = queue.popleft()
                for ro, co in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    fr, fc = r_ + ro, c_ + co
                    if 0 <= fr < row and 0 <= fc < col and grid[fr][fc] == "1" and (fr, fc) not in visited:
                        visited.add((fr, fc))
                        queue.append((fr, fc))

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        

        return islands