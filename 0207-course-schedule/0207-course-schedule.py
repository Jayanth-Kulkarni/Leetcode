class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create an adj list for all the courses
        # create an empty list for all courses, will remain empty if there are prereqs
        map = {course:[] for course in range(numCourses)}

        # Run through the prereq list and fill in the map
        for course, prereq in prerequisites:
            map[course].append(prereq)

        # Create a visited set to track the nodes visited in the gaph's path
        visited = set()

        # Dfs function to figure out loops in the gaph's path 
        def dfs(node):
            # if node in visited, return False
            if node in visited:
                return False

            # if a course doesn't have any prereqs then it can be completed
            if map[node] == []:
                return True
            
            visited.add(node)

            for prereq in map[node]:
                if not dfs(prereq): return False

            # Remove the node from the path
            visited.remove(node)

            # Mark the map[node] as empty as we have verified all prereqs
            map[node] = []

            # Return True, as we looped through all the prereqs all were able to complete
            return True


        # Run a for loop over all the courses and call the dfs function for it.
        for course in map:
            if not dfs(course): return False
        
        return True