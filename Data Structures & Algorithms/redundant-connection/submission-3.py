class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {v:-1 for v in range(1, len(edges)+1)}

        def find(u):
            if parent[u] == -1:
                return u
            else:
                parent[u] = find(parent[u])
                return parent[u]
        

        for u, v in edges:
            parent_u = find(u)
            parent_v = find(v)

            if parent_u == parent_v:
                return [u, v]
            
            parent[parent_u] = parent_v