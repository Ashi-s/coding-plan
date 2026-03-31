class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx = float('-inf')

        summ = 0
        for n in nums:
            summ += n
            maxx = max(maxx, summ)
            if summ < 0:
                summ = 0
        return maxx
        