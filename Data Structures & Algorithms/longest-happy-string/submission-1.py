class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        res = ''

        if a > 0:
            heapq.heappush_max(maxHeap, (a, 'a'))
        if b > 0:
            heapq.heappush_max(maxHeap, (b, 'b'))
        if c > 0:
            heapq.heappush_max(maxHeap, (c, 'c'))

        while maxHeap:
            count, char = heapq.heappop_max(maxHeap)
            
            # check last two char is same
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxHeap:
                    break
                count2, char2 = heapq.heappop_max(maxHeap)
                res += char2

                # add previous back
                if count > 0:
                    heapq.heappush_max(maxHeap, (count, char)) 
                if count2 - 1 > 0:
                    heapq.heappush_max(maxHeap, (count2 - 1, char2)) 
                
            else:
                res += char
                if count - 1 > 0:
                    heapq.heappush_max(maxHeap, (count - 1, char)) 
            
        
        return res
