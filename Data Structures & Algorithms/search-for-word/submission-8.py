class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M, N = len(board), len(board[0])
        
        def helper(r, c, visited, idx):
            if idx == len(word):
                self.res = True
                return

            dir = [(r, c+1), (r, c-1), (r-1, c), (r+1, c)]

            for row, col in dir:
                if 0 <= row < M and 0 <= col < N and (row, col) not in visited and board[row][col] == word[idx]:
                    visited.add((row, col))
                    helper(row, col, visited, idx+1)
                    visited.remove((row, col))


        self.res = False
        for i in range(M):
            for j in range(N):
                if board[i][j] == word[0]:
                    visited = set()
                    visited.add((i, j))
                    helper(i, j, visited, 1)
        
        return self.res