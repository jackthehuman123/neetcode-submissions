class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        for r in range(ROWS):
            for c in range(r, ROWS):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        for r in range(ROWS):
            matrix[r].reverse()
