class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = []
        queue = deque()
        row, col = len(image), len(image[0])
        original_color = image[sr][sc]
        image[sr][sc] = color
        visited.append([sr,sc])
        queue.append([sr,sc])
        directions = ((0,1),(0,-1),(1,0),(-1,0))
        while len(queue) > 0:
            sr, sc = queue.popleft()
            for direction in directions:
                new_sr, new_sc = sr + direction[0], sc + direction[1]
                if 0 <= new_sr < row and 0 <= new_sc < col and [new_sr, new_sc] not in visited and image[new_sr][new_sc] == original_color:
                    image[new_sr][new_sc] = color
                    queue.append([new_sr, new_sc])
                    visited.append([new_sr, new_sc])
        return image
