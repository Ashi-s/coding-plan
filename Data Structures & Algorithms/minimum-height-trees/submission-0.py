class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(n)}

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        #BFS
        def bfs(root, parent):
            q = deque()
            q.append((root, parent))
            height = 0

            while q:
                size = len(q)
                height += 1
                for i in range(size):
                    node, parent = q.popleft()
                    for nei in adj[node]:
                        if parent != nei:
                            q.append((nei, node))
            
            minAdj[height] = minAdj.get(height, [])
            minAdj[height].append(root)
            self.minHeight = min(self.minHeight, height)
        
        self.minHeight = n
        minAdj = {} #height: [nodes]
        
        for i in range(n):
            bfs(i, -1)
        
        return minAdj[self.minHeight]
