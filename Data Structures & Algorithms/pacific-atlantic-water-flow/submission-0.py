class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        visitP = set()
        visitA = set()
        def dfs(row, col, cur, visit):
            if (row < 0 or col < 0 or 
                row >= ROWS or col >= COLS or
                (row, col) in visit):
                return 
            if cur > heights[row][col]:
                return
            
            visit.add((row, col))
            dfs(row + 1, col, heights[row][col], visit)
            dfs(row - 1, col, heights[row][col], visit)
            dfs(row, col + 1, heights[row][col], visit)
            dfs(row, col - 1, heights[row][col], visit)
        
        for c in range(COLS):
            dfs(0, c, heights[0][c], visitP)
            dfs(ROWS-1, c, heights[ROWS-1][c], visitA)

        for r in range(ROWS):
            dfs(r, 0, heights[r][0], visitP)
            dfs(r, COLS-1, heights[r][COLS-1], visitA)

        return list(visitA & visitP)

            

            