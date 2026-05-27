class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {c:[] for c in range(numCourses)}

        for a, b in prerequisites:
            adj[a].append(b)
        

        def helper(crs):
            
            if crs in processed:
                return True
            
            if crs in visited: #cycle
                return False
            
            visited.add(crs)
            for p in adj[crs]:
                if not helper(p):
                    return False
            
            processed.add(crs)
            visited.remove(crs)

            return True


        visited = set() # current
        processed = set() # completed

        for crs in range(numCourses):
            if not helper(crs):
                return False
        
        return True