class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # TLE O(n^2)
        N = len(nums)
        res = float('inf')
        for i in range(N):
            summ = 0
            for j in range(i, N):
                summ += nums[j]
                if summ >= target:
                    res = min(res, j-i+1)
                    break
        
        return res if res != float('inf') else 0

        # N = len(nums)
        # left = 0
        # summ = 0
        # res = float('inf')

        # for right in range(N):
        #     summ += nums[right]

        #     while summ >= target:
        #         res = min(res, right - left + 1)
        #         summ -= nums[left]
        #         left += 1
        
        # return res if res != float('inf') else 0
        