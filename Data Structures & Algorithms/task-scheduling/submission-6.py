class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0

        d = {}
        for t in tasks:
            d[t] = d.get(t, 0) + 1
        
        maxHeap = []
        for key, val in d.items():
            heapq.heappush_max(maxHeap, (val, key))
        
        q = deque()

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt, task = heapq.heappop_max(maxHeap)

                if cnt - 1 > 0:
                    q.append((cnt-1, task, time+n))
            
            while q and q[0][2] == time:
                count, ttask, ttime = q.popleft()
                heapq.heappush_max(maxHeap, (count, ttask))
        
        return time
            
