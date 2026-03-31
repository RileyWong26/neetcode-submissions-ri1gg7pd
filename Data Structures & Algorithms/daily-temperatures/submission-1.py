class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [[] for n in temperatures]
        s = []
        for i,temp in enumerate(temperatures):
            
            # Check new element greater than top of stack
            while len(s) > 0 and temp > s[-1][0]:
                # Add difference at the index
                res[s[-1][1]] = i - s[-1][1]
                s.pop(-1)
            
            s.append((temp, i))

            
            
            
        # handle last temperatures
        while len(s) > 0:
            temp, i = s.pop(-1)
            res[i] = 0
            
        return res
                

            