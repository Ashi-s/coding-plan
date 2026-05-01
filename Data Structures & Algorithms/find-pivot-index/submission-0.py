class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = [-1]*len(nums), [-1]*len(nums)

        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            left[i] = curr
        
        curr = 0
        for i in range(len(nums)-1, -1, -1):
            curr += nums[i]
            right[i] = curr
        
        for i in range(len(nums)):
            if left[i] == right[i]:
                return i
        
        return -1
        