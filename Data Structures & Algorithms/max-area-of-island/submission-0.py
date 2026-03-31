class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def helper(r, c, curr):
            dir = [(r, c-1), (r, c+1), (r-1, c), (r+1, c)]

            for row, col in dir:
                if 0 <= row < M and 0 <= col < N and grid[row][col] == 1:
                    grid[row][col] = '#'
                    curr.append(1)
                    helper(row, col, curr)
        

        M, N = len(grid), len(grid[0])
        _max = 0

        for row in range(M):
            for col in range(N):
                if grid[row][col] == 1:
                    grid[row][col] = '#'
                    curr = [1]
                    helper(row, col, curr)
                    _max = max(_max, sum(curr))
        
        return _max