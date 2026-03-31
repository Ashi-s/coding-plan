class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}

        for t in tasks:
            d[t] = d.get(t, 0) + 1
        
        res = 0
        maxHeap = []
        q = deque()

        for key, value in d.items():
            heapq.heappush_max(maxHeap, (value, key))
        
        while maxHeap or q:
            res += 1
            
            if maxHeap:
                count, task = heapq.heappop_max(maxHeap)
                if count - 1 > 0:
                    q.append((count-1, res + n, task))  # cooldowm is current time + n
            
            
            #insert from q back to maxHeap after cooldown
            if q and q[0][1] == res:
                count, time, task = q.popleft()
                heapq.heappush_max(maxHeap, (count, task))
        
        return res
        

