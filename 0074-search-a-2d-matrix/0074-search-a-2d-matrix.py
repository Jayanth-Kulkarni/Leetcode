class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        row,col = 0, m-1
        while (row<n and row>=0 and col<m and col>=0):
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
        return False
    	        
    	