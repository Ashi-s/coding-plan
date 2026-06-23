class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()

        _sum = prices[0] + prices[1]
        if _sum <= money:
            return money - _sum
        else:
            return money