class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(x: int, y: int) -> bool:
            # Out of bounds
            if x < 0 or y < 0 or x >= ROWS or y >= COLS:
                return

            # Not an O
            if board[x][y] != "O":
                return

            # an O mark as visted and unsurroundable
            if board[x][y] == "O":
                print(x, y)
                board[x][y] = "#"
            
            # Try all surrounding guys
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)

        # Check borders
        for i in range(ROWS):
            dfs(i, COLS -1)
            dfs(i, 0)
        for i in range(COLS):
            dfs(ROWS -1, i)
            dfs(0, i)

        # mark unvisted as X
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"