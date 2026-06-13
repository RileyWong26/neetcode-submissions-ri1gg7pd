class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        maxL, maxR = [0 for i in range(N)], [0 for i in range(N)]
        
        # Find maxes on both sides
        for i in range(1, N):
            maxL[i] = max(maxL[i-1], height[i-1])
            maxR[-(i+1)] = max(maxR[-i], height[-i])
        
        print(maxL, maxR)
        
        res = 0
        # find hte highest position at each guy
        for i in range(N):
            if height[i] < min(maxL[i], maxR[i]):
                res += min(maxL[i], maxR[i]) - height[i]


        return res