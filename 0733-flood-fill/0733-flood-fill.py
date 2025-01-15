class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = deque()
        r, c = len(image), len(image[0])
        oc = image[sr][sc]
        image[sr][sc] = color
        directions = [(0,-1), (0,1), (-1,0), (1,0)]
        queue.append([sr, sc])
        visited = set()
        visited.add((sr, sc))
        while len(queue) > 0:
            new_r, new_c = queue.popleft()
            for dr, dc in directions:
                nr, nc = new_r + dr, new_c + dc
                print(nr, nc, dr, dc)
                if 0 <= nr < r and 0 <= nc < c and image[nr][nc] == oc and (nr, nc) not in visited :
                    image[nr][nc] = color
                    queue.append([nr, nc])
                    visited.add((nr,nc))
        return image