class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(n) for n in nums]

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] + nums[i] > nums[i] + nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        
        # edge case if all zero (more than 1) [0, 0, 0]
        if nums[0] == '0':
            return "0"
        return ''.join(nums)