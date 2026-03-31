class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        _sum = 0
        res = float('-inf')

        for n in nums:
            _sum += n
            res = max(res, _sum)
            if _sum < 0:
                _sum = 0
        return res
        