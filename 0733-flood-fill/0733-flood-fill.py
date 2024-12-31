class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = []
        visited = []
        queue.append([sr,sc,image[sr][sc]])
        image[sr][sc] = color
        visited.append([sr,sc])
        while(len(queue)>0):
            sr,sc,compare_color = queue.pop(0)
            if [sr-1,sc] not in visited and sr-1>=0 and image[sr-1][sc] == compare_color:
                queue.append([sr-1,sc,image[sr-1][sc]])
                image[sr-1][sc] = color
                visited.append([sr-1,sc])
            if [sr+1,sc] not in visited and sr+1<len(image) and image[sr+1][sc]== compare_color:
                queue.append([sr+1,sc,image[sr+1][sc]])
                image[sr+1][sc] = color
                visited.append([sr+1,sc])
            if [sr,sc-1] not in visited and sc-1>=0 and image[sr][sc-1]== compare_color:
                queue.append([sr,sc-1,image[sr][sc-1]])
                image[sr][sc-1] = color
                visited.append([sr,sc-1])
            if [sr,sc+1] not in visited and sc+1<len(image[0]) and image[sr][sc+1]== compare_color:
                queue.append([sr,sc+1,image[sr][sc+1]])
                image[sr][sc+1]= color
                visited.append([sr,sc+1])
        
        return image