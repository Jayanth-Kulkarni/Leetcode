class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        map = defaultdict(list)
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
        
        for course in range(numCourses):
            if dfs(course) == False:
                return False
        
        return True