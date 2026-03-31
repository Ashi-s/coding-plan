class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n

        def dfs(i):
            if i >= n:
                return 0
            
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = max(nums[i] + dfs(i+2), dfs(i+1))
            return memo[i]
        
        return dfs(0)

        # TLE - Recursion
        # self.res = 0
        # def dfs(i, curr):
        #     if i >= len(nums):
        #         self.res = max(self.res, curr)
        #         return
            
        #     #pick
        #     dfs(i+2, curr+nums[i])

        #     #dont pick
        #     dfs(i+1, curr)
        
        
        # dfs(0, 0)
        # return self.res
        