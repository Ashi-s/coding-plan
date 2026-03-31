class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)


        while len(stones) > 0:
            if len(stones) == 1:
                return stones[0]
            first = heapq.heappop_max(stones)
            second = heapq.heappop_max(stones)

            if first > second:
                heapq.heappush_max(stones, first-second)
        
        return 0