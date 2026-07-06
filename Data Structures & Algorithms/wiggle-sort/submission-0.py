class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = []
        nums.sort()

        l, r = 0, len(nums)-1

        while l < r:
            if nums[l] > nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
            l += 1
            
            if l < r:
                if nums[r] > nums[l]:
                    nums[l], nums[r] = nums[r], nums[l]
                l += 1
               
                