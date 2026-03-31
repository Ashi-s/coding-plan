class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        l, r = 0, 1
        _max = 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                _max = max(_max, prices[r] - prices[l])
            
            r += 1
        
        return _max
