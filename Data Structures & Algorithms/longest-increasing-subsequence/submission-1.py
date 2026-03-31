class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def dfs(idx):

            if memo[idx] != -1:
                return memo[idx]
            
            LIS = 1
            for j in range(idx+1, N):
                if nums[j] > nums[idx]:
                    LIS = max(LIS, 1 + dfs(j))

            memo[idx] = LIS
            return memo[idx]
        
        N = len(nums)
        memo = [-1] * N
    
        for i in range(N):
            dfs(i)

        return max(memo)