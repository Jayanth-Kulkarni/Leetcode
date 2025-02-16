class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        island = 0
        visited = set()
        def dfs(ro, co):
            queue = deque()
            queue.append((ro, co))
            visited.add((ro,co))
            while queue:
                r_, c_ = queue.popleft()
                for r1, c1 in [(1,0), (-1,0), (0,1), (0,-1)]:
                    r = r1 + r_
                    c = c1 + c_
                    if 0 <= r < row and 0 <= c < col and grid[r][c] == "1" and (r,c) not in visited:
                        visited.add((r,c))
                        queue.append((r,c))

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    island += 1
        
        return island