class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c = 0, len(matrix[0])-1
        row, col = len(matrix), len(matrix[0])
        while 0 <= c < col and 0 <= r < row:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c-=1
            else:
                r+=1
        return False