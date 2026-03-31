class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights) - 1
        highest = 0

        while p1 <= p2:

            width = p2 - p1
            height = min(heights[p2], heights[p1])

            highest = max(width * height, highest)

            if heights[p1] <= heights[p2]:
                p1 += 1
            else:
                p2 -= 1
            
        
        return highest