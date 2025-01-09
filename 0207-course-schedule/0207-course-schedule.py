class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # form the adj list
        map = {course:[] for course in range(numCourses)}
        
        # fill the adj list
        for course, prereq in prerequisites:
            map[course].append(prereq)

        # visited set to detect loops
        visited = set()

        # dfs to identify loops
        def dfs(course):

            # if there are no prereqs, that course can be completed
            if map[course] == []:
                return True

            # if a loop is found return False
            if course in visited:
                return False

            # Add the current course to the path (incompleted visited!)
            visited.add(course)

            # Run loop-checker for all the prereq for that course
            for prereq in map[course]:
                if not dfs(prereq): return False 

            # Remove the course from the visited set, as it's completed
            visited.remove(course)

            # Remove all prereqs in the map
            map[course] = []

            return True

        for course in range(numCourses):
            if not dfs(course): return False

        return True