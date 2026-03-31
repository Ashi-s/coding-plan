class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # TLE time O(n2)

        # res = 0

        # for i in range(len(nums)):
        #     _sum = 0
        #     for j in range(i, len(nums)):
        #         _sum += nums[j]
        #         print(_sum)
        #         if _sum == k:
        #             res += 1
        # return res

        prefixSum = {0:1}
        summ = 0
        res = 0

        for n in nums:
            summ += n

            if (summ - k) in prefixSum:
                res += prefixSum[summ-k]
            
            prefixSum[summ] = prefixSum.get(summ, 0) + 1
        
        return res



        