class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = [[] for i in range(numCourses)]

        for c, pre in prerequisites:
            courses[c].append(pre)

        visited = set()
        def dfs(curr):
            if curr in visited:
                return False
            elif courses == []:
                return True
            visited.add(curr)
            
            for p in courses[curr]:
                if not dfs(p):
                    return False
            visited.remove(curr)
            courses[curr] = []

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True

        
