class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = col = 9
        for i in range(row):
            seen = set()
            for j in range(col):
                if board[i][j] in seen:
                    return False
                if not board[i][j] == ".": 
                    seen.add(board[i][j])
        for j in range(col):
            seen = set()
            for i in range(row):
                if board[i][j] in seen:
                    return False
                if not board[i][j] == ".": 
                    seen.add(board[i][j])

        boxes = {}
        for i in range(3):
            for j in range(3):
                boxes[(i, j)] = set()
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == ".":
                    continue 
                if board[i][j] in boxes[((i // 3), (j// 3))]:
                    return False
                else:
                    boxes[((i // 3), (j// 3))].add(board[i][j])
        
        return True