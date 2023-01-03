class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        visited = [False] * numCourses
        stack = []
        for course in range(numCourses):
            if not visited[course]:
                if not self.dfs(course, graph, visited, stack):
                    return False
        
        return True
    
    def dfs(self, course, graph, visited, stack):
        visited[course] = True
        stack.append(course)
        for prereq in graph[course]:
            if visited[prereq]:
                if prereq in stack:
                    return False
            else:
                if not self.dfs(prereq, graph, visited, stack):
                    return False
        stack.pop()
        return True
