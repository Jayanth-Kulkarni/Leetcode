class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        row, col = len(grid), len(grid[0])
        visited = set()
        iteration = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visited.add((r, c))

        while len(queue) > 0:
            for _ in range(len(queue)):
                r_, c_ = queue.popleft()
                for ro, co in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                    r, c = ro + r_, co + c_
                    if 0 <= r < row and 0 <= c < col and (r, c) not in visited and grid[r][c] == 1:
                        grid[r][c] = 2
                        queue.append((r, c))
                        visited.add((r, c))
            if len(queue) > 0:
                iteration += 1
        
        complete = True
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    complete = False
                    break
        return iteration if complete else -1