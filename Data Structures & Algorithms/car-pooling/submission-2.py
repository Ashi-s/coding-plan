class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key= lambda x:x[1])

        curr = 0
        minHeap = [] #(end, pas)

        for t in trips:
            pas, start, end = t

            while minHeap and minHeap[0][0] <= start:
                curr -= minHeap[0][1]
                heapq.heappop(minHeap)
            
            curr += pas
            if curr > capacity:
                return False
            
            heapq.heappush(minHeap, (end, pas))
        
        return True