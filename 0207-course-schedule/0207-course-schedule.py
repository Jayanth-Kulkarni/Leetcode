class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        map = {course:[] for course in range(numCourses)}

        for course, prereq in prerequisites:
            map[course].append(prereq)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            
            if map[course] == []:
                return True
            
            visited.add(course)

            for prereq in map[course]:
                if dfs(prereq) == False:
                    return False 

            visited.remove(course)
            
            map[course] = []

            return True

        for course in map:
            if not dfs(course):
                return False 

        return True