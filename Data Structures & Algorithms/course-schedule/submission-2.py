class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Hold pre requesites for each course in an array
        pre = [[] for i in range(numCourses)]

        for course, prereq in prerequisites:
            pre[course].append(prereq)
        

        def dfs(curr, visited):
            visited.append(curr)
            for p in pre[curr]:
                if p in visited:
                    return False 
                elif not dfs(p, visited.copy()):
                    return False
            return True
        
        for i in range(numCourses):
            if not dfs(i, []):
                return False
        return True
