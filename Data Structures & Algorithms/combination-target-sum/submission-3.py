class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        def helper(idx, curr, total):
            if idx >= len(nums):
                return
            if total > target:
                return
            
            if total == target:
                res.append(curr.copy())
                return
            
            curr.append(nums[idx])
            helper(idx, curr, total+nums[idx])

            curr.pop()
            helper(idx+1, curr, total)
        
        res = []
        helper(0, [], 0)
        return res