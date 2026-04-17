class Solution:
    def climbStairs(self, n: int) -> int:
        # Array showing how many ways to get to each step 
        pos = [-1 for i in range(n)] 
        # Initialize first two positions
        if len(pos) >= 1:
            pos[0] = 1     # 1 step
            if len(pos) >=2:
                pos[1] = 2     # 2 step and 1+1 step
        
        for i in range (2, len(pos)):
            pos[i] = pos[i-2] + pos[i-1]
        
        return pos[-1]

        
        