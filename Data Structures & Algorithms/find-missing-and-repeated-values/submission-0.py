class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = [0, 0]

        n = len(grid)
        d = {}

        for i in range(n):
            for j in range(len(grid[0])):
                d[grid[i][j]] = 1 + d.get(grid[i][j], 0)

        for i in range(1, n**2 + 1):
            if i not in d:
                ans[1] = i
            elif d[i] == 2:
                ans[0] = i
            
        
        return ans
