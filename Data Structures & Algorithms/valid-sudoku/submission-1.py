class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols ={}
        rows = {}
        box = {}

        # Iterate through rows
        for i in range(0, 9):
            # iterate through cols
            for j in range(0, 9):
                curr = board[i][j]

                # Add to cols
                if curr != ".":
                    if j not in cols:
                        cols[j] = set()
                    elif curr in cols[j] :
                        return False
                    cols[j].add(curr)

                    # Add to rows
                    if i not in rows:
                        rows[i] = set()
                    elif curr in rows[i]:
                        return False
                    rows[i].add(curr)

                    # Grid
                    grid_row = i // 3
                    grid_col = j // 3
                    if grid_row not in box:
                        box[grid_row] = {grid_col : set()}
                    elif grid_col not in box[grid_row]:
                        box[grid_row][grid_col] = set()
                    elif curr in box[grid_row][grid_col]:
                        return False
                    box[grid_row][grid_col].add(curr)
                
        
        return True