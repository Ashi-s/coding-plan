class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increase = 1
        decrease = 1

        increase_count = 1
        decrease_count = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                increase += 1
            else:
                increase = 1
            increase_count = max(increase_count, increase)
        
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                decrease += 1
            else:
                decrease = 1
            decrease_count = max(decrease_count, decrease)
        
        return max(increase_count, decrease_count)
            