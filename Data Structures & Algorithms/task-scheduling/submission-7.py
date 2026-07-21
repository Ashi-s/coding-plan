class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}
        for t in tasks:
            d[t] = d.get(t, 0) + 1
        
        maxHeap = []
        for task, count in d.items():
            heapq.heappush_max(maxHeap, (count, task))
        
        q = deque()
        time = 0

        while maxHeap or q:
            time += 1
            if maxHeap:
                count, task = heapq.heappop_max(maxHeap)

                if count - 1 > 0:
                    q.append((count-1, task, time+n))
            
            while q and q[0][2] == time:
                cnt, tsk, ttime = q.popleft()
                heapq.heappush_max(maxHeap, (cnt, tsk))
        
        return time