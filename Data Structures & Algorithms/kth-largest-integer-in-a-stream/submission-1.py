class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.maxHeap = []
        
        for num in nums:
            heapq.heappush_max(self.maxHeap, num)
        

    def add(self, val: int) -> int:
        heapq.heappush_max(self.maxHeap, val)

        output = []
        for i in range(self.k):
            output.append(heapq.heappop_max(self.maxHeap))
        
        answer = output[-1]

        for num in output:
            heapq.heappush_max(self.maxHeap, num)
        
        return answer

