class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        for i in range(len(nums)):
            curr = nums[i]
            for j in range(i+1, len(nums)):
                curr += nums[j]
                if curr % k == 0:
                    return True
        
        return False