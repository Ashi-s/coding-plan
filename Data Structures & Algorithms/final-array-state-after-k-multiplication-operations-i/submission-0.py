class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        minHeap = []

        for i in range(len(nums)):
            heapq.heappush(minHeap, (nums[i], i))
        

        for i in range(k):
            val, idx = heapq.heappop(minHeap)
            heapq.heappush(minHeap, (val*multiplier, idx))
        
        res = [0]*len(nums)
        for val, idx in minHeap:
            res[idx] = val
        
        return res