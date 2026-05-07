class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc, dec = True, True

        # increasing
        for i in range(1, len(nums)):
            if nums[i-1] <= nums[i]:
                continue
            else:
                inc = False
                break

        # decreasing
        for j in range(len(nums)-2, -1, -1):
            if nums[j+1] <= nums[j]:
                continue
            else:
                dec = False
                break
        
        return inc or dec

