class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def helper(r, c):
            if r == m-1 and c == n-1:
                self.count += 1
                return

            dir = [(r, c+1), (r+1, c)]

            for row, col in dir:
                if row >= 0 and row < m and col >= 0 and col < n:
                    helper(row, col)
        
        self.count = 0
        helper(0, 0)
        return self.count