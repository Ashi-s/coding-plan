class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        _res = nums[0]

        currMin, currMax = 1, 1
        for n in nums:
            tmp = n * currMax
            currMax = max(currMax*n, currMin*n, n)
            currMin = min(tmp, currMin*n, n)

            _res = max(_res, currMax)
        
        return _res
        