class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def helper(idx, curr):
            if idx == len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[idx])
            helper(idx+1, curr)

            curr.pop()
            helper(idx+1, curr)
        
        res = []
        helper(0, [])
        return res