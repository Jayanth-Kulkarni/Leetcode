class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        visited = set()
        def dfs(i, r, c):
            if i == len(word):
                return True
            
            if not (0<= r < row and 0 <= c < col and board[r][c] == word[i] and (r,c) not in visited) :
                return False
            visited.add((r,c))
            res = dfs(i+1, r-1, c) or dfs(i+1, r+1, c) or dfs(i+1, r, c+1) or dfs(i+1, r, c-1)
            visited.remove((r,c))
            return res
        for r in range(row):
            for c in range(col):
                if dfs(0, r, c) == True:
                    return True
        
        return False