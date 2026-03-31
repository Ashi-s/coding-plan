class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def helper(idx, summ, curr):
            if summ == target:
                res.append(curr.copy())
                return
            
            if idx >= len(candidates) or summ > target:
                return 
            
            curr.append(candidates[idx])
            helper(idx+1, summ+candidates[idx], curr)


            while idx+1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx += 1
            curr.pop()
            helper(idx+1, summ, curr)
        
        res = []
        candidates.sort()
        helper(0, 0, [])
        return res