class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(x, y, steps):
            # Check out of bounds
            if x >= ROWS or x < 0 or y >= COLS or y <0:
                return 
            # Water back?
            if grid[x][y] == -1:
                return 
            
            if grid[x][y] < steps:
                return 
            
            grid[x][y] = steps 
            dfs(x+1, y, steps + 1)
            dfs(x-1, y, steps + 1)
            dfs(x, y-1, steps + 1)
            dfs(x, y+1, steps + 1)
            
            return 

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    dfs(i, j, 0)
