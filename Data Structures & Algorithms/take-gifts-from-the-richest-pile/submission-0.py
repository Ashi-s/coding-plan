import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxHeap = []

        for g in gifts:
            heapq.heappush_max(maxHeap, g)
        
        for i in range(k):
            gift = heapq.heappop_max(maxHeap)

            reduce = math.floor(math.sqrt(gift))

            heapq.heappush_max(maxHeap, reduce)

        return sum(maxHeap)