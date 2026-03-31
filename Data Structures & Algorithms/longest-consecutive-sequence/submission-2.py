class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        nums.sort()
        count = 1
        _max = 0

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                count += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                count = 1
            _max = max(_max, count)
            print(count, _max)
        return max(_max, count)

            




                
        
        