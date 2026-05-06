class Solution:
    def climbStairs(self, n: int) -> int:
        stairs = [0] *n

        for i in range(n-1,-1, -1):
            
            if n - i == 2:
                stairs[i] = 2
            elif n-i == 1:
                stairs[i] = 1
            else:
                stairs[i] = stairs[i+2] + stairs[i+1]

        return stairs[0]
        
        