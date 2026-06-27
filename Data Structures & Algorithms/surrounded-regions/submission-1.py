class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visit = set()
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O":
                    visit.add((row, col))

        def dfs(row, col):
            if (row < 0 or col < 0 or
                row >= ROWS or col >= COLS or 
                board[row][col] == "X" or (row, col) not in visit):
                return

            visit.remove((row, col))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1) 

        for r, c in visit:
            board[r][c] = "X"
        






