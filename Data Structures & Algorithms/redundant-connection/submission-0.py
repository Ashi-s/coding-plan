class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = { v:-1 for v in range(1, len(edges)+1)}
        print(parent)
        def find(u):
            print(f"parent-{u}={parent[u]}")
            if parent[u] == -1:
                return u
            else:
                return find(parent[u])
        
        for u, v in edges:
            parent_u = find(u)
            parent_v = find(v)
            print(parent_u, parent_v)
            if parent_u == parent_v:
                return [u, v]
            else:
                parent[parent_v] = parent_u
            print(parent)
        