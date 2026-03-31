class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}

        for u,v in prerequisites:
            adj[u].append(v)
        

        def helper(crs):
            if crs in visited:
                return False
            
            if crs in processed:
                return True
            
            visited.add(crs)

            for pre in adj[crs]:
                if not helper(pre):
                    return False
                
            visited.remove(crs)
            processed.add(crs)
            output.append(crs)

            return True
        
        visited = set()
        processed = set()
        output = []
        for crs in range(numCourses):
            if not helper(crs):
                return []
        
        return output



        