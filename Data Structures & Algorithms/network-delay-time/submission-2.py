class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Adj list 
        adj = {i: [] for i in range(n+1)}
        for u, v, t in times:
            adj[u].append([t, v])

        print(adj)
        
        minHeap = [[0, k]]
        visited = set()

        res = 0
        while len(minHeap) != 0:
            t, c = heapq.heappop(minHeap)
            if c in visited:
                continue

            visited.add(c)
            res = max(res, t)
            for t2,n2 in adj[c]:
                heapq.heappush(minHeap, [t2+t, n2])

        return res if len(visited) == n else -1