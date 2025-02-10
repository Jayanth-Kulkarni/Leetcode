class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        row, col = len(grid), len(grid[0])
        island = 0

        def dfs(ro,co):
            queue = deque()
            queue.append((ro,co))
            while len(queue) > 0:
                ro, co = queue.popleft()
                for r_, c_ in [(1,0), (-1,0), (0,1), (0,-1)]:
                    r = ro + r_
                    c = co + c_
                    if 0 <= r < row and 0 <= c < col and grid[r][c] == "1":
                        grid[r][c] = "2"
                        queue.append((r,c))                    


        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    dfs(r,c)
                    island += 1
        
        return island