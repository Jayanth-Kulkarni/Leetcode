class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        map = {course: [] for course in range(numCourses)}
        for course, prerequisite in prerequisites:
            map[course].append(prerequisite)
        
        visited = set()
        

        def dfs(course):
            if map[course] == []:
                return True
            
            if course in visited:
                return False
            
            visited.add(course)

            for prereq in map[course]:
                if not dfs(prereq):
                    return False
            
            visited.remove(course)

            map[course] = []

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True