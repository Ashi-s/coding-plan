class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        n = len(nums)

        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                return abs(num)
            else:
                nums[idx] *= -1
        return -1