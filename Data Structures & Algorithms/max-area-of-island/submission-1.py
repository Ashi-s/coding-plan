class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def helper(r, c, count):
            dir = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]

            for row, col in dir:
                if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 1:
                    grid[row][col] = '#'
                    count.append(1)
                    helper(row, col, count)


        _max = 0
        ROWS, COLS = len(grid), len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    grid[i][j] = '#'
                    count = [1]
                    helper(i, j, count)
                    _max = max(_max, sum(count))
        
        return _max