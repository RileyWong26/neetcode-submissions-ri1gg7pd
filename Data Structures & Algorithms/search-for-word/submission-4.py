class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        N = len(word)

        directions = [[0,1], [1,0], [-1, 0], [0, -1]]

        visited = {i: set([]) for i in range(ROWS)}
        
        def dfs(x, y, pos):
            if pos == N:
                return True
            if x < 0 or x == ROWS or y < 0 or y == COLS:
                return False
            
            if board[x][y] != word[pos] or y in visited[x]:
                return False
            
            visited[x].add(y)

            for dx, dy in directions:
                if dfs(x + dx, y + dy, pos+1):
                    return True

            visited[x].remove(y)
            return False
            

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):

                    return True

        return False
