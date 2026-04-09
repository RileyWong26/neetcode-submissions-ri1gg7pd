class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(x, y, count):
            if x < 0 or y < 0 or y >= COLS or x >= ROWS:
                return 0
            
            if grid[x][y] == 1 :
                print(grid[x][y])
                grid[x][y] = 0
                
                count += 1
                count += dfs(x - 1, y, 0)
                count += dfs(x + 1, y, 0)
                count += dfs(x, y - 1, 0)
                count += dfs(x, y + 1, 0)
                return count
            
            return 0


        res = 0

        for i in range (ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j, 0))

        return res                    