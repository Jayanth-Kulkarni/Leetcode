class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = deque()
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        nr, nc = len(grid), len(grid[0])
        time = 0

        # Add all initially rotten oranges to the queue
        for row in range(nr):
            for col in range(nc):
                if grid[row][col] == 2:
                    queue.append((row, col))
                    visited.add((row, col))
        
        # BFS to spread rot
        while queue:
            for _ in range(len(queue)):  # Process current level
                r_, c_ = queue.popleft()
                for dr, dc in directions:
                    r, c = r_ + dr, c_ + dc
                    if 0 <= r < nr and 0 <= c < nc and grid[r][c] == 1 and (r, c) not in visited:
                        grid[r][c] = 2
                        visited.add((r, c))
                        queue.append((r, c))
            if queue:  # Only increment time if there are oranges being processed
                time += 1

        # Check if there are any fresh oranges left
        for row in range(nr):
            for col in range(nc):
                if grid[row][col] == 1:
                    return -1

        return time