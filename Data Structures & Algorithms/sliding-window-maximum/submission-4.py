class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        maxHeap = []

        for i in range(k):
            heapq.heappush_max(maxHeap, (nums[i], i))
        
        if maxHeap:
            res.append(maxHeap[0][0])

        for i in range(k, len(nums)):
            heapq.heappush_max(maxHeap, (nums[i], i))
            while maxHeap[0][1] <= i - k:
                heapq.heappop_max(maxHeap)

            res.append(maxHeap[0][0])
            
        return res