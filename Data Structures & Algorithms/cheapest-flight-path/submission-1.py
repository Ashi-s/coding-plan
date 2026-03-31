class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjency = {}

        for i in range(len(flights)):
            fro, to, price = flights[i]

            if fro not in adjency:
                adjency[fro] = [(price, to)]
            else:
                adjency[fro].append((price, to))
        
        minCost = [float('inf')] * n
        minCost[src] = 0

        q = deque([(0, src, 0)]) # price, to, stop

        while q:
            price, node, stops = q.popleft()

            if stops > k:
                continue
            
            for p, to in adjency.get(node, []):
                if price + p < minCost[to]:
                    minCost[to] = price+p
                    q.append((price+p, to, stops+1))
        
        if minCost[dst] != float('inf'):
            return minCost[dst]
        else:
            return -1

