class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0
        def dfs(row, col):
            if (row < 0 or col < 0 or
                row >= ROWS or col >= COLS or 
                grid[row][col] == 0):
                return 0
            grid[row][col] = 0
            return (1 + dfs(row + 1, col)
            + dfs(row - 1, col)
            + dfs(row, col + 1)
            + dfs(row, col - 1))
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    maxArea = max(maxArea, dfs(row, col))
        return maxArea