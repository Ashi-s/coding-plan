class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return n
        
        i, j = 0, 0

        while i < len(nums) and j < len(nums) :
            nums[i] = nums[j]
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            i = i + 1
        return i
            


        