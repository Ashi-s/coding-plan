class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}

        for u, v, t in times:
            if u not in adj:
                adj[u] = [(v, t)]
            else:
                adj[u].append((v, t))
        
        minHeap = [(0, k)]
        visited = set()
        res = float('inf')

        while minHeap:
            time, node = heapq.heappop(minHeap)

            if node in visited:
                continue
                
            res = time
            
            visited.add(node)
            
            for nei, t in adj.get(node, []):
                if nei not in visited:
                    heapq.heappush(minHeap, (time+t, nei))
        
        if len(visited) == n:
            return res
        else:
            return -1