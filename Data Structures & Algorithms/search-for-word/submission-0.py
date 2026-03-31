class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def helper(r, c, idx):

            if len(res) > 0:
                return

            if idx >= len(word):
                res.append(visited.copy())
                return 
            dir = [(r, c-1), (r, c+1), (r-1, c), (r+1, c)]
            
            for row, col in dir:
                if row >= 0 and col >= 0 and row < len(board)  and col < len(board[0]) and (row, col) not in visited and board[row][col] == word[idx]:
                    visited.append((row,col))
                    helper(row, col, idx+1)
                    visited.pop()
        

        res = []
        visited = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = [(i, j)]
                    helper(i, j, 1)
        
        print(res)
        return len(res) > 0
        