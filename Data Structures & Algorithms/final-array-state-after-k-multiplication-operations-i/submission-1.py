class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        minHeap = []
        res = nums[:]

        for i in range(len(nums)):
            heapq.heappush(minHeap, (nums[i], i))
        

        for i in range(k):
            val, idx = heapq.heappop(minHeap)
            value = val*multiplier
            res[idx] = value
            heapq.heappush(minHeap, (value, idx))
    
        return res