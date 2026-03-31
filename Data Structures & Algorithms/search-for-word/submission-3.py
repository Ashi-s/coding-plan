class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def helper(r, c, idx):
            if len(output) > 0:
                return
            
            if idx >= len(word):
                output.append(visited.copy())
                return
            
            for row, col in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                dr, dc = row + r, col + c

                if 0 <= dr < ROWS and 0 <= dc < COLS and (dr, dc) not in visited and board[dr][dc] == word[idx]:
                    visited.add((dr, dc))
                    helper(dr, dc, idx + 1)
                    visited.remove((dr, dc))


        ROWS, COLS = len(board), len(board[0])
        output = []

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    visited = set()
                    visited.add((i, j))
                    helper(i, j, 1)
        
        return len(output) > 0