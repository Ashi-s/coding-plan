class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = 0

        for i in range(len(nums)):
            summ = 0
            for j in range(i, len(nums)):
                summ += nums[j]

                if summ == goal:
                    res += 1
        
        return res