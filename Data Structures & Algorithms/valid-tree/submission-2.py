class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        neighbors = [[] for i in range(n)]

        # Add Neighbors
        for n1, n2 in edges:
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)
        
        visited = set()
        print(neighbors)
        def dfs(prev: int, curr: int): 
            if curr in visited:
                return False

            visited.add(curr)

            # Traversal
            for neighbor in neighbors[curr]:
                if neighbor == prev:
                    continue
                if not dfs(curr, neighbor):
                    return False
            return True
        return dfs(-1, 0) and n == len(visited)