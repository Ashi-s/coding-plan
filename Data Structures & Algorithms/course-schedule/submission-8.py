class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}

        for u, v in prerequisites:
            adj[u].append(v)

        
        def helper(crs):
            
            if not adj[crs]: # no pre-req
                return True

            if crs in processed:
                return True

            if crs in visited: # means cycle
                return False
            
            visited.add(crs)
            for pre in adj[crs]:
                if not helper(pre):
                    return False
                    
            # visited.remove(crs)
            processed.add(crs)
            return True

        
        visited = set()
        processed = set()
        for crs in range(numCourses):
            if not helper(crs):
                return False
        return True
        
        