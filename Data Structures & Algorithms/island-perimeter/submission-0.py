class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        # each box add 4 as perimeter
        # but if top and left then subtract 2
        # perimeter = 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == 1:
        #             perimeter += 4
                
        #             # top
        #             if (i-1) >= 0 and grid[i-1][j] == 1:
        #                 perimeter -= 2
                    
        #             #left
        #             if (j-1) >= 0 and grid[i][j-1] == 1:
        #                 perimeter -= 2
        
        # return perimeter


        # DFS 
        def dfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
                return 1
            
            if (r, c) in visited:
                return 0
            
            visited.add((r, c))
            
            # up, down, left, right
            perim = dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)
            return perim
        
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)
        
        return 0