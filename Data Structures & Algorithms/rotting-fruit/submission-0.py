from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        fresh = 0
        q = deque()
        time = 0

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))
        
        dir = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        while fresh > 0 and q:
            n = len(q)
            for i in range(n):
                row, col = q.popleft()

                for dr, dc in dir:
                    r, c = row + dr, col + dc
                    if 0 <= r < M and 0 <= c < N and grid[r][c] == 1:
                        grid[r][c] = 2
                        fresh -= 1
                        q.append((r, c))
            
            time += 1
        
        return time if fresh == 0 else -1


