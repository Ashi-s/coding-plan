class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjency = {i: [] for i in range(numCourses)}

        for a, b in prerequisites:
            adjency[a].append(b)
        
        def helper(crs):
            if crs in cycle:
                return False
            
            if crs in visited:
                return True
            
            cycle.add(crs)
            for p in adjency[crs]:
                if not helper(p):
                    return False
            visited.add(crs)
            cycle.remove(crs)
            output.append(crs)
            return True

        
        visited = set()
        cycle = set()
        output = []
        for crs in adjency:
            if not helper(crs):
                return []
        return output


        