class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = 0, len(matrix[0])
        row, col = len(matrix), len(matrix[0])
        print(r,c,row,col)
        while 0 <= r < row and 0 <= c < col:
            if matrix[r][c] == target:
                return True
            if matrix[r][c] < target:
                c -= 1
            else:
                r += 1
        return False