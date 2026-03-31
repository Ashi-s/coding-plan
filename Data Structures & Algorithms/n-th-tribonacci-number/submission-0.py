class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        
        memo = [-1] * (n+1)
        memo[0] = 0
        memo[1] = memo[2] = 1

        def dfs(i):
            if i > n:
                return 0

            if memo[i] != -1:
                return memo[i]
            
            memo[i] = dfs(i-1) + dfs(i-2) + dfs(i-3)
            return memo[i]
        
        return dfs(n)
