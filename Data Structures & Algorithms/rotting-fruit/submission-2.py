class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()

        fresh = 0
        output = 0
        M, N = len(grid), len(grid[0])
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j, 0))
        
        while fresh > 0 and q:
            n = len(q)
            for i in range(n):
                row, col, val = q.popleft()

                dir = [(0, -1), (0, 1), (-1, 0), (1, 0)]

                for r, c in dir:
                    if 0 <= (row+r) < M and 0 <= (col+c) < N and grid[row+r][col+c] == 1:
                        fresh -= 1
                        grid[row+r][col+c] = 2
                        q.append((row+r, col+c, val+1))
            output += 1
        
        if fresh > 0:
            return -1
        
        return output
        