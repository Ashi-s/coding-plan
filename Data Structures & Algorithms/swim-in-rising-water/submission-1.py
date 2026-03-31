class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        minHeap = [(grid[0][0], 0, 0)] # elevation/time, row, col

        visited = set()

        while minHeap:
            time, r, c = heapq.heappop(minHeap)

            if r == N-1 and c == N-1:
                return time
            
            visited.add((r,c))
            
            directions = [(r, c+1), (r, c-1), (r-1, c), (r+1, c)]

            for row, col in directions:
                if 0 <= row < N and 0 <= col < N and (row, col) not in visited:
                    heapq.heappush(minHeap, (max(time, grid[row][col]) ,row, col))