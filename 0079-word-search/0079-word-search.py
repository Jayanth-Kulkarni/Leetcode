class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        
        def dfs(r, c, cur):
            cur += board[r][c][0]
            if cur != word[:len(cur)] or visited[r][c]:
                return
            if cur == word:
                return True
            visited[r][c] = True
            if r+1 < row:
                if dfs(r+1,c,cur): return True
            if r-1 >= 0:
                if dfs(r-1,c,cur): return True
            if c+1 < col:
                if dfs(r,c+1,cur): return True
            if c-1 >= 0:
                if dfs(r,c-1,cur): return True
            visited[r][c] = False
        visited = [[False for _ in range(col)] for _ in range(row)]
        for r in range(row):
            for c in range(col):
                visited[r][c] = False
                if dfs(r, c, ""):
                    return True
        return False