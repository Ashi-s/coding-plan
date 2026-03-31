class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            maxHeap.append([dist, x, y])
        
        heapq.heapify_max(maxHeap)
        
        while len(maxHeap) > k:
            heapq.heappop_max(maxHeap)
        
        return [[x,y] for d, x, y in maxHeap]
        