class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        _max = max(piles)
        l, r = 1, _max
        k = _max

        while l <= r:
            m = (l + r) // 2

            hour = 0
            for p in piles:
                hour += math.ceil(p / m)
            
            if hour <= h:
                k = m
                r = m - 1
            else:
                l = m + 1
        
        return k



