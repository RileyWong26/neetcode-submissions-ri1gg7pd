class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = [] 
        res = 0

        for h in heights:
            s2 = []
            popped = 0 
            while len(s) != 0 and s[-1] > h:
                # Change the value to be smallest possible
                val = s.pop(-1)
                s2.append(h)
                popped +=1
                # see if have a rect
                res = max(res, popped * val)
            while len(s2) > 0:
                s.append(s2.pop(-1))
            
            s.append(h)
        
        N = len(s)
        for i in range(N):
            res = max(res, s[i] * (N-i))
        
        return res