class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        
        queue = deque()
        fresh = 0
        max_time = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh += 1
        
        while queue:
            r, c, t = queue.popleft()
            max_time = max(t, max_time)

            for r_, c_ in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                r1 = r_ + r
                c1 = c_ + c
                if 0<= r1 < row and 0<= c1 < col and grid[r1][c1] == 1:
                    fresh -= 1
                    grid[r1][c1] = 2
                    queue.append((r1, c1, t+1))
        
        if fresh == 0:
            return max_time
        else:
            return -1