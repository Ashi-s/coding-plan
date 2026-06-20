class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(idx, curr, res):

            if len(curr) == k:
                res.append(curr.copy())
                return
            
            if idx >= n:
                return
            
            #pick
            curr.append(idx+1)
            helper(idx+1, curr, res)

            curr.pop()
            helper(idx+1, curr, res)


        res = []
        for i in range(1, n-k+2):
            helper(i, [i], res)
        
        return res