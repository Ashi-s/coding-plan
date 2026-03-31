class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def helper(idx, summ, curr):
            
            if summ == target:
                res.append(curr.copy())
                return

            if idx >= len(nums) or summ > target:
                return 
            
            curr.append(nums[idx])
            helper(idx, summ + nums[idx], curr)

            curr.pop()
            helper(idx+1, summ, curr)
        
        res = []
        helper(0, 0, [])
        return res