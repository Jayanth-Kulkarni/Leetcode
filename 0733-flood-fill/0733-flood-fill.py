class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = []
        original_color = image[sr][sc]
        queue.append([sr,sc])
        image[sr][sc] = color
        visited = [[sr,sc]]
        while len(queue) > 0:
            sr,sc = queue.pop() 
            if sr-1>=0 and [sr-1,sc] not in visited and image[sr-1][sc] == original_color:
                visited.append([sr-1,sc])
                queue.append([sr-1,sc])
                image[sr-1][sc] = color
            if sr+1<len(image) and [sr+1,sc] not in visited and  image[sr+1][sc] == original_color:
                visited.append([sr+1,sc])
                queue.append([sr+1,sc])
                image[sr+1][sc] = color
            if sc-1>=0 and [sr,sc-1] not in visited and image[sr][sc-1] == original_color:
                visited.append([sr,sc-1])
                queue.append([sr,sc-1])
                image[sr][sc-1] = color
            if sc+1<len(image[0]) and [sr,sc+1] not in visited and image[sr][sc+1] == original_color:
                visited.append([sr,sc+1])
                queue.append([sr,sc+1])
                image[sr][sc+1] = color
        return image