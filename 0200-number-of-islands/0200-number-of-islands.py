class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = set()
        island = 0

        def bfs(r, c):
            queue = deque()
            queue.append((r,c))
            while len(queue) > 0:
                r, c = queue.popleft()
                for r_, c_ in [(1,0), (-1,0), (0,1), (0,-1)]:
                    ro, co = r + r_, c + c_
                    if 0 <= ro < row and 0 <= co < col and grid[ro][co] == "1" and (ro, co) not in visited:
                        queue.append((ro,co))
                        visited.add((ro,co))


        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r,c)
                    island += 1
        

        return island