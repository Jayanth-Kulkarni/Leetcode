class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        queue = deque()
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r,c))
        

        count = 0
        while len(queue) > 0:
            level = len(queue)
            for i in range(level):
                ro, co = queue.popleft()
                for r_, c_ in [(1,0), (-1,0), (0,1), (0,-1)]:
                    r = ro + r_
                    c = co + c_
                    if 0 <= r < row and 0 <= c < col and grid[r][c] == 1:
                        grid[r][c] = 2
                        queue.append((r,c))
            
            if len(queue) > 0:
                count += 1

        flag = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    flag = 1
                    break
        
        if flag:
            return -1
        
        return count