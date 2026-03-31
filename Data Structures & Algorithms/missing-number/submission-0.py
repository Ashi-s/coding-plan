class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        curr, total = 0, 0

        for i in range((len(nums) + 1)):
            total += i
        
        for i in nums:
            curr += i
        
        return total - curr