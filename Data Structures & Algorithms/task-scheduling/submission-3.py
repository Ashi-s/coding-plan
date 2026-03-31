class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}

        for t in tasks:
            counts[t] = counts.get(t, 0) + 1
        
        maxHeap = []
        for key, val in counts.items():
            heapq.heappush_max(maxHeap, (val, key))
        
        q = deque()
        time = 0

        while maxHeap or q:
            time += 1

            if maxHeap:
                count, task = heapq.heappop_max(maxHeap)
                if count - 1 > 0:
                    q.append((count-1, time+n, task)) # add cooldown period


            # add back the top of q back to heap after cooldown
            if q and q[0][1] == time:
                cnt, val, task = q.popleft()
                heapq.heappush_max(maxHeap, (cnt, task))
        
        return time