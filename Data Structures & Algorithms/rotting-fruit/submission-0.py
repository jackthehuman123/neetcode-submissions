from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    q.append((row, col))
        time = 0
        while q:
            n = len(q)
            rotted = False
            for _ in range(n):
                row, col = q.popleft()
                for nr, nc in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 1):
                        continue
                    rotted = True
                    grid[nr][nc] = 2
                    q.append((nr, nc))
            if rotted:
                time += 1

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    return -1
        return time  
                
