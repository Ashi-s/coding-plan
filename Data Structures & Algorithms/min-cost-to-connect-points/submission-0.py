class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        adjency = {i:[] for i in range(N)}

        for i in range(N):
            xi, yi = points[i]
            for j in range(i+1, N):
                xj, yj = points[j]
                manh = abs(xi-xj) + abs(yi-yj)
                adjency[i].append((manh, j))
                adjency[j].append((manh, i))
        
        
        minHeap = [(0, 0)]
        visited = {}
        res = 0

        while minHeap:
            distance, node = heapq.heappop(minHeap)
            print(distance, node)
            print(visited)

            if node in visited:
                continue
            
            visited[node] = distance
            res += distance

            for dist, nei in adjency[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, (dist, nei))
        
        return res
        