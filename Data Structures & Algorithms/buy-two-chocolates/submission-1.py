class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # O(NLogN)

        # prices.sort()

        # _sum = prices[0] + prices[1]
        # if _sum <= money:
        #     return money - _sum
        # else:
        #     return money

        # O(N)
        min1, min2 = float('inf'), float('inf')

        for p in prices:
            if p < min1:
                min1, min2 = p, min1
            elif p < min2:
                min2 = p
        
        if (min1 + min2) <= money:
            return money - (min1 + min2)
        else:
            return money
