class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        def helper():
            if len(nums) == len(curr):
                res.append(curr.copy())
                return
            
            for i in nums:
                if i not in curr:
                    curr.append(i)
                    helper()
                    curr.pop()
            
        helper()
        return res
        