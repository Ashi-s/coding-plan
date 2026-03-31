class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjency = {}

        for u, v, t in times:
            if u not in adjency:
                adjency[u] = [(v, t)]
            else:
                adjency[u].append((v, t))
        
        minHeap = [(0, k)]
        visited = {}
        _max = float('inf') # we don't have to do max(visited.values())

        while minHeap:
            time, node = heapq.heappop(minHeap)

            if node in visited:
                continue
            
            _max = time
            visited[node] = time
            
            for nei, t in adjency.get(node, []):
                if nei not in visited:
                    heapq.heappush(minHeap, (time+t, nei))
        
        if len(visited) == n:
            max_val = max(visited.values())
            print(f"Verifying single variable for max: {_max}")
            return max_val
        else:
            return -1

        

        