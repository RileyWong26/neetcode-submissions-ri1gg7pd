class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Hold edges for each node
        edgelist = [[] for i in range(n)]
        
        # add edges
        for n1, n2 in edges:
            edgelist[n1].append(n2)
            edgelist[n2].append(n1)

        visited = set()

        def dfs(curr):
            # Base case return if visted.
            if curr in visited:
                return
            
            # Add to visited
            visited.add(curr)
            
            # Traverse all edges
            for edge in edgelist[curr]:
                dfs(edge)
            
        res = 0
        # Traverse all noders
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        
        return res




