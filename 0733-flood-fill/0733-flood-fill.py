class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # collect the rows and cols that are = 1 in the queue
        queue = deque()
        row, col = len(image), len(image[0])
        original_color = image[sr][sc]
        image[sr][sc] = color
        queue.append((sr, sc))
        visited = set()
        while len(queue) > 0:
            ro, co =  queue.popleft()
            for r_, c_ in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                r, c = ro + r_, co + c_
                if 0 <= r < row and 0 <= c < col and image[r][c] == original_color and (r, c) not in visited:
                    image[r][c] = color
                    queue.append((r, c))
                    visited.add((r,c))
        
        return image