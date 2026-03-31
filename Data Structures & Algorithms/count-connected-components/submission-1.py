class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = {i:-1 for i in range(n)}
        count = n
        
        def find(u):
            if parent[u] == -1:
                return u
            else:
                return find(parent[u])
        

        for u, v in edges:
            parent_u = find(u)
            parent_v = find(v)

            if parent_v != parent_u:
                parent[parent_v] = parent_u
                count -= 1
        
        return count
        