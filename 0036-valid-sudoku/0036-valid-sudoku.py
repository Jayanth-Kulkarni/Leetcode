class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col = len(board), len(board[0])
        rd, cd, sd = defaultdict(set), defaultdict(set), defaultdict(set)
        for r in range(row):
            for c in range(col):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rd[r] or board[r][c] in cd[c] or board[r][c] in sd[(r//3,c//3)]):
                    return False
                rd[r].add(board[r][c])
                cd[c].add(board[r][c])
                sd[(r//3,c//3)].add(board[r][c])
        return True