class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0:1}
        res = 0
        summ = 0

        for i in range(len(nums)):
            summ += nums[i]

            if (summ - k) in d: # if diff exists
                res += d[summ - k]
            
            if summ in d:
                d[summ] += 1
            else:
                d[summ] = 1
        
        return res