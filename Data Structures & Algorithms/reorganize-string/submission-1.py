class Solution:
    def reorganizeString(self, s: str) -> str:
        d = {}

        for i in s:
            d[i] = d.get(i, 0) + 1
        
        q = deque()
        maxHeap = []
        time = 0
        for k, v in d.items():
            heapq.heappush_max(maxHeap, (v, k))
        
        res = ''

        while maxHeap:
            if not q and len(maxHeap) == 1 and maxHeap[0][0] > 1:
                return ""

            time += 1
            count, key = heapq.heappop_max(maxHeap)

            if count - 1 > 0:
                q.append((count-1, key, time+1))
            
            res += key
            print(res)

            while q and q[0][2] == time:
                cnt, vl, t = q.popleft()
                heapq.heappush_max(maxHeap, (cnt, vl))
        
        return res