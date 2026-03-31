class MedianFinder:

    def __init__(self):
        self.minHeap = [] # right part
        self.maxHeap = [] # left part

    def addNum(self, num: int) -> None:
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush_max(self.maxHeap, num)
        
        minHeap_len = len(self.minHeap)
        maxHeap_len = len(self.maxHeap)
        
        if minHeap_len > maxHeap_len + 1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush_max(self.maxHeap, val)
        elif maxHeap_len > minHeap_len + 1:
            val = heapq.heappop_max(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        

    def findMedian(self) -> float:
        minHeap_len = len(self.minHeap)
        maxHeap_len = len(self.maxHeap)

        if minHeap_len > maxHeap_len:
            return self.minHeap[0]
        elif maxHeap_len > minHeap_len:
            return self.maxHeap[0]
        else:
            return (self.minHeap[0] + self.maxHeap[0]) / 2.0

        
        
        