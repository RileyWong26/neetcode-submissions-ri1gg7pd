class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Hold pre requesites for each course in an array
        pre = [[] for i in range(numCourses)]

        for course, prereq in prerequisites:
            pre[course].append(prereq)
        
        visited = set()
        def dfs(curr):
            if curr in visited:
                return False
            if pre[curr] == []:
                return True 
            visited.add(curr)
            for p in pre[curr]:
                if p in visited:
                    return False 
                elif not dfs(p):
                    return False
            visited.remove(curr)
            pre[curr] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
