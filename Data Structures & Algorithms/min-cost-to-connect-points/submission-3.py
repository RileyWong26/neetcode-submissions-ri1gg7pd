class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj  = {i: [] for i in range(len(points))}

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]

                dist = abs(x1 - x2) + abs(y1 - y2)
                
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        visited = set()
        res = 0
        shortest = [[0,0]]
        while len(visited) != len(points):
            dist, a = heapq.heappop(shortest)

            if a in visited:
                continue

            for child in adj[a]:
                heapq.heappush(shortest, child)
            visited.add(a)
            
            res += dist
        
        return res