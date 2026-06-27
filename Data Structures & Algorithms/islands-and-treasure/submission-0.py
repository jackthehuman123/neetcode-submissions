from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        q = deque()
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    q.append((row, col))
        
        while q:
            row, col = q.popleft()
            for r, c in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                if (r < 0 or c < 0 or 
                    r >= ROWS or c >= COLS
                    or grid[r][c] != INF):
                    continue
                grid[r][c] = grid[row][col] + 1
                q.append((r, c))


