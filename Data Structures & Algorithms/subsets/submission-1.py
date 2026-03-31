class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(idx, curr):
            if idx >= len(nums):
                output.append(curr.copy())
                return
            
            #pick
            curr.append(nums[idx])
            helper(idx+1, curr)

            # don't pick
            curr.pop()
            helper(idx+1, curr)
        

        output = []
        helper(0, [])
        return output