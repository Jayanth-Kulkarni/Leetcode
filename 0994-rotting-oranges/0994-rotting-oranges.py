class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        row, col = len(grid), len(grid[0])
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r,c))
        
        iterations = -1
        while len(queue):
            length = len(queue)
            for _ in range(length):
                ro, co = queue.popleft()
                for r_, c_ in [(1,0), (-1,0), (0,1), (0,-1)]:
                    r, c = ro+r_, co+c_
                    if 0 <= r < row and 0 <= c < col and grid[r][c] == 1:
                        queue.append((r,c))
                        grid[r][c] = 2
            iterations += 1
            length = len(queue)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    return -1

        return iterations if iterations > -1 else 0