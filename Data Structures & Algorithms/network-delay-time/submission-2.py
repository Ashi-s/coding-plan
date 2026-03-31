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

        while minHeap:
            time, node = heapq.heappop(minHeap)

            if node in visited:
                continue
            
            visited[node] = time

           
            
            for nei, t in adjency.get(node, []):
                if nei not in visited:
                    heapq.heappush(minHeap, (time+t, nei))
        
        if len(visited) == n:
            max_val = max(visited.values())
            return max_val
        else:
            return -1

        

        