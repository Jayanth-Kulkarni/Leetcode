class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = set()
        islands = 0
        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r,c))
            while queue:
                ro, co = queue.popleft()
                for r_, c_ in [(1,0), (-1,0), (0, 1), (0, -1)]:
                    r1 = ro + r_
                    c1 = co + c_
                    if 0 <= r1 < row and 0 <= c1 < col and (r1, c1) not in visited and grid[r1][c1] == "1":
                        visited.add((r1, c1))
                        queue.append((r1, c1))

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        
        return islands