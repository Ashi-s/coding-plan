class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        path = {i:[] for i in range(numCourses)}

        for a, b in prerequisites:
            path[a].append(b)
        
        def helper(crs):
            
            if not path[crs]: # course has no pre-req []
                return True
            
            if crs in visited: # cycle
                return False
            
            visited.add(crs)
            for p in path[crs]:
                if not helper(p):
                    return False
            visited.remove(crs)
            
            path[crs] = [] # memoization - once a courses is traversed, we can skip them for next rounds
            return True
        
        visited = set()
        for crs in range(numCourses):
            if not helper(crs):
                return False
        
        return True
        
            
        