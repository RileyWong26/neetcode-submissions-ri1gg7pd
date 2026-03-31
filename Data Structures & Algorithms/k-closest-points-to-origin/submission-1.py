class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Create a max heap
        hp = []
        heapq.heapify_max(hp)

        for point in points:
            euclid = math.sqrt((0-point[0])**2 + (0-point[1])**2)
            # add if < k
            if len(hp) < k:
                heapq.heappush_max(hp, (euclid, point))
            # Check if new point is smaller than the max 
            else:
                # Calculate distances
                max_point = heapq.heappop_max(hp)
                euclid_max = max_point[0]
                # Add if a closer point
                if euclid < euclid_max:
                    heapq.heappush_max(hp, (euclid, point))
                else:
                    heapq.heappush_max(hp, max_point)

        res = []
        while len(hp) > 0:
            curr = heapq.heappop_max(hp)
            res.append(curr[1])
        return res