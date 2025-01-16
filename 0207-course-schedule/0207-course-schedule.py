class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create the adj list for the graph
        map = {courses: [] for courses in range(numCourses)}

        # Fill the map with prereqs
        for course, prereq in  prerequisites:
            map[course].append(prereq)

        # Create a visited set to check for loops
        visited = set()

        # Perform DFS using this function
        def dfs(course):

            # if already visited (loop) return False
            if course in visited:
                return False
            
            # If all the prereqs are complated return True
            if map[course] == []:
                return True
                
            visited.add(course)            
            # Loop through all the prereq and make sure it can be completed
            for prereq in map[course]:
                if not dfs(prereq):
                    return False
            
            # Remove the course from visited list as it can be completed
            visited.remove(course)

            # Mark the prereqs for this course as empty, as it can be completed
            map[course] = []

            return True
        
        for course in map:
            if not dfs(course):
                return False

        return True

            

