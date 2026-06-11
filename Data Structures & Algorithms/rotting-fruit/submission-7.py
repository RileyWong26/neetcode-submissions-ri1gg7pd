class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        
        ROWS,COLS = len(grid), len(grid[0])

        oj = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append([i, j])
                elif grid[i][j] == 1:
                    oj += 1

        res = 0
        while len(queue) > 0  and oj> 0:
            for i in range(len(queue)):
                x,y = queue.pop(0)
                
                if (x - 1) >= 0 and grid[x-1][y] == 1:
                    queue.append([x-1, y])
                    grid[x-1][y] = 2
                    oj -= 1
                if (x + 1) < ROWS and grid[x+1][y] == 1:
                    queue.append([x+1, y])
                    grid[x+1][y] = 2
                    oj -= 1
                if (y - 1) >= 0 and grid[x][y-1] == 1:
                    queue.append([x, y-1])
                    grid[x][y-1] = 2
                    oj -= 1
                if (y + 1) < COLS and grid[x][y+1] == 1:
                    queue.append([x, y + 1])
                    grid[x][y+1] = 2
                    oj -= 1
            res += 1
            

        return -1 if oj != 0 else res    
     