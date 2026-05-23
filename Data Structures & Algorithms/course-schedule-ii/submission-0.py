class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre = [[] for i in range(numCourses)]

        for crs, prereq in prerequisites:
            pre[crs].append(prereq)
        
        res = []
        visit, cycle = set(), set()

        def dfs(curr):
            if curr in cycle:
                return False
            if curr in visit:
                return True
            cycle.add(curr)

            for prereq in pre[curr]:
                if not dfs(prereq):
                    return False
            
            cycle.remove(curr)
            visit.add(curr)
            res.append(curr)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []

        return res