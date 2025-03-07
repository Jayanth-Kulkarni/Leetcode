class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        row, col = len(grid), len(grid[0])
        res = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    q.append((r,c))
        
        while q:
            for i in range(len(q)):
                r_, c_ = q.popleft()
                for r1, c1 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    r = r_ + r1
                    c = c_ + c1
                    if 0 <= r < row and 0 <= c < col and grid[r][c] == 1:
                        grid[r][c] = 2
                        q.append((r,c))
            if len(q) > 0:
                res+= 1
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:        
                    return -1
        return res
            