class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = { c: [] for c in range(numCourses)}

        for u, v in prerequisites:
            adj[u].append(v)

        def helper(crs):
            if not adj[crs]: # no pre-req
                return True
            
            if crs in processed:
                return True
            
            if crs in visited: # cycle
                return False

            visited.add(crs)

            for p in adj[crs]:
                if not helper(p):
                    return False
            
            processed.add(crs)
            return True
        

        visited = set()
        processed = set()

        for crs in range(numCourses):
            if not helper(crs):
                return False
        
        return True