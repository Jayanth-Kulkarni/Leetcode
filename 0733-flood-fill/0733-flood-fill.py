class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row, col = len(image), len(image[0])
        queue = deque()
        queue.append((sr, sc))
        oc = image[sr][sc]
        image[sr][sc] = color
        visited = set((sr,sc))
        while queue:
            r1, c1 = queue.popleft()
            for r_, c_ in [(1,0), (-1, 0), (0,1), (0,-1)]:
                r, c = r1 + r_, c1 + c_
                if 0 <= r < row and 0 <= c < col and image[r][c] == oc and (r,c) not in visited:
                    image[r][c] = color
                    queue.append((r,c))
                    visited.add((r,c)) 
        return image