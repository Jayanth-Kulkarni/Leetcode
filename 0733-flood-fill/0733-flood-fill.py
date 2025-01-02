class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        queue = [[sr,sc]]
        image[sr][sc] = color
        visited = [[sr,sc]]
        while len(queue) > 0:
            sr,sc = queue.pop()
            if sr-1 >= 0 and [sr-1,sc] not in visited and image[sr-1][sc] == original_color:
                image[sr-1][sc] = color
                queue.append([sr-1,sc])
                visited.append([sr-1,sc])
            if sr+1 < len(image) and [sr+1,sc] not in visited and image[sr+1][sc] == original_color:
                image[sr+1][sc] = color
                queue.append([sr+1,sc])
                visited.append([sr+1,sc])
            if sc-1 >= 0 and [sr,sc-1] not in visited and image[sr][sc-1] == original_color:
                image[sr][sc-1] = color
                queue.append([sr,sc-1])
                visited.append([sr,sc-1])
            if sc+1 < len(image[0]) and [sr,sc+1] not in visited and  image[sr][sc+1] == original_color:
                image[sr][sc+1] = color
                queue.append([sr,sc+1])
                visited.append([sr,sc+1])
        return image