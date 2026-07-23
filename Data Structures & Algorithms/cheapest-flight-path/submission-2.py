class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # dict from: (price, to)
        adjency = {}

        for flight in flights:
            frm, to, price = flight

            if frm not in adjency:
                adjency[frm] = [(price, to)]
            else:
                adjency[frm].append((price, to))
        
        minPrice = [float('inf')] * n
        minPrice[src] = 0

        q = deque()
        q.append((0, src, 0)) #price, from, stop

        while q:
            price, frm, stops = q.popleft()

            if stops > k:
                continue
            
            for p, to in adjency.get(frm, []):
                if p + price < minPrice[to]:
                    minPrice[to] = p + price
                    q.append((p+price, to, stops+1))
                    
        
        if minPrice[dst] != float('inf'):
            return minPrice[dst]
        else:
            return -1