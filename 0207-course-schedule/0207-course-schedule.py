class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create the adj list for the graph

        adj = {course:[] for course in range(numCourses)}
        for course, prereq in prerequisites:
            adj[course].append(prereq)

        # to find the loop
        visited = set()

        def dfs(course):
            if adj[course] == []:
                return True
            
            if course in visited:
                return False

            visited.add(course)
            for prereq in adj[course]:
                if not dfs(prereq):
                    return False

            visited.remove(course)
            adj[course] = []

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True