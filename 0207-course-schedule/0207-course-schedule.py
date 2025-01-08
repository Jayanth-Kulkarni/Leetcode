class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # Create an empty list for each course
        map = {i:[] for i in range(numCourses)}
        
        # Fill in the list for each course with it's prereq
        # In case the prereq list is empty, then that course can be completed!
        for course, prereq in prerequisites:
            map[course].append(prereq)

        # Initialize a visited set, to keep track of all the courses that were previously visited
        # If the course can be completed, remove it from visited list. 
        visited = set()

        def dfs(course):
            # If we come accross the same course again, before it get's removed then return False
            if course in visited:
                return False

            # If the prepreq for that course is empty, then return True
            if map[course] == []:
                return True
            
            # Add the course to visited list
            visited.add(course)

            # Keep calling all the prereqs of that course to see if there is a loop
            for pre in map[course]:

                # # Return false as soon as the function returns false
                if not dfs(pre): return False

            # If all the prepreqs were completed without any loop, then remove it from the visited set
            visited.remove(course)

            # Make the map[course] as empty, as we visited all the prereqs
            map[course] = []

            # Return true, as that course can now be completed!
            return True

        # For all the course in the map recursively call dfs
        for course in map:
            
            # Return false as soon as the function returns false
            if not dfs(course): return False
        
        return True
            
