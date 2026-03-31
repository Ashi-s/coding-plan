class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def helper(r, c):
            dir = [(r, c-1), (r, c+1), (r-1, c), (r+1, c)]

            for row, col in dir:
                if 0 <= row < M and 0 <= col < N and grid[row][col] == '1':
                    grid[row][col] = '#'
                    helper(row, col)
        

        M, N = len(grid), len(grid[0])
        count = 0

        for row in range(M):
            for col in range(N):
                if grid[row][col] == '1':
                    grid[row][col] = '#'
                    count += 1
                    helper(row, col)
        
        return count
        