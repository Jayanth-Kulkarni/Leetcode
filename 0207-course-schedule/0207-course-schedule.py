class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        map = {i:[] for i in range(numCourses)}

        visited = set()

        for course, prereq in prerequisites:
            map[course].append(prereq)
        
        def dfs(course):

            if course in visited:
                return False
            
            if map[course] == []:
                return True
            
            visited.add(course)
            
            for prereq in map[course]:
                if not dfs(prereq):
                    return False

            visited.remove(course)

            map[course] = []

            return True
        
        for course in map:
            if not dfs(course):
                return False

        return True