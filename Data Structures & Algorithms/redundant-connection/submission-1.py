class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {i:-1 for i in range(1, len(edges)+1)}

        def find(u):
            if parent[u] == -1:
                return u
            else:
                return find(parent[u])
        
        for u, v in edges:
            parent_u = find(u)
            parent_v = find(v)

            if parent_u == parent_v:
                return [u,v]
            else:
                parent[parent_v] = parent_u