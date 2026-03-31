class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        width = len(matrix[0])
        height = len(matrix)
        # Binary search for rows 
        l = 0
        r = height

        while l != r:
            mid = (r - l) // 2 + l 

            row = matrix[mid]

            # Check if current row may contain 
            if row[0] <= target and row[-1] >= target: 
                # Binary search the row
                l = 0 
                r = width 

                while l != r: 
                    mid = (r - l) // 2 + l

                    if row[mid] == target:
                        return True
                    # In right subarray
                    elif row[mid] < target: 
                        l = mid + 1 
                    else:
                        r = mid      
                return False

            # Move up in rows 
            elif row[-1] > target: 
                r = mid 
            # move down 
            else:
                l = mid + 1
        

        return False
        