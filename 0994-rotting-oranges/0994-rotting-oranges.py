class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        queue = deque()
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i, j))
        
        while queue:
            level = len(queue)
            for i in range(level):
                r1, c1 = queue.popleft()
                for r_, c_ in [(1,0), (-1,0), (0, 1), (0, -1)]:
                    r = r1 + r_
                    c = c1 + c_
                    if 0 <= r < row and 0 <= c < col and grid[r][c] == 1:
                        grid[r][c] = 2
                        queue.append((r,c))      
            if len(queue):
                res += 1
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1
        return res
            