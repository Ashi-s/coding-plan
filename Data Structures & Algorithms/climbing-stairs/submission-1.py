class Solution:
    def climbStairs(self, n: int) -> int:

        # Recurion - TLE

        # def helper(i, curr):
        #     if i == n:
        #         res.append(1)
        #         return
        #     if i > n:
        #         return 
            
        #     # curr.append(1)
        #     helper(i+1, curr+1)
        #     # curr.pop()

        #     # curr.append(2)
        #     helper(i+2, curr+2)
        #     # curr.pop()
        
        # res = []
        # helper(0, 0)
        # return len(res)

        # DP - Top Down
        cache = [-1] * n
        def dfs(i):
            if i == n:
                return 1
            if i > n:
                return 0
            
            if cache[i] != -1:
                return cache[i]
            
            cache[i] = dfs(i+1) + dfs(i+2)
            return cache[i]
        
        return dfs(0)
       
            
        