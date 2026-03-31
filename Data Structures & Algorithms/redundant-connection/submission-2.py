class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = {v:-1 for v in range(1, n+1)}

        def find(u):
            if parent[u] == -1:
                return u
            else:
                return find(parent[u])
        
        for u, v in edges:
            parent_u = find(u)
            parent_v = find(v)

            if parent_u == parent_v:
                return [u, v]
            
            parent[parent_v] = parent_u