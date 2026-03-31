class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        minHeap = []
        pt_Heap = []
        time = 0
        output = []

        for i, task in enumerate(tasks):
            heapq.heappush(minHeap, (task[0], task[1], i))
        
        while minHeap or pt_Heap:
            while minHeap and minHeap[0][0] <= time:
                et, pt, i = heapq.heappop(minHeap)
                heapq.heappush(pt_Heap, (pt, i))
            
            if not pt_Heap:
                time = minHeap[0][0]
            else:
                process_t, index = heapq.heappop(pt_Heap)
                time += process_t
                output.append(index)
        
        return output