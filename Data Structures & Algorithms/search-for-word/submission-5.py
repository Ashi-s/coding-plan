class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def helper(r, c, idx, visited):
            if len(output) > 0: # early exit
                return
            if idx >= len(word):
                output.append(word)
                return
            dirs = [(r, c+1), (r, c-1), (r+1, c), (r-1, c)]

            for row, col in dirs:
                if 0 <= row < M and 0 <= col < N and (row, col) not in visited and board[row][col] == word[idx]:
                    visited.append((row, col))
                    helper(row, col, idx+1, visited)
                    visited.pop()



        M, N = len(board), len(board[0])
        output = []

        for i in range(M):
            for j in range(N):
                if len(output) > 0: # early exists if we found the word
                    return True
                if board[i][j] == word[0]:
                    visited = [(i, j)]
                    helper(i, j, 1, visited)
        
        return len(output) > 0