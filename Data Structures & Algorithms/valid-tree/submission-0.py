class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = {v:-1 for v in range(n)}
        node = n

        def find(u):
            if parent[u] == -1:
                return u
            else:
                return find(parent[u])
        
        for u, v in edges:
            parent_u = find(u)
            parent_v = find(v)

            if parent_u == parent_v:
                return False

            node -= 1

            parent[parent_v] = parent_u
        
        return node == 1