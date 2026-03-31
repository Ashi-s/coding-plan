class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        def helper(r, c):
            dir = [(r, c-1), (r, c+1), (r-1, c), (r+1, c)]
            for row, col in dir:
                if 0 <= row < M and 0 <= col < N and board[row][col] == 'O':
                    board[row][col] = '#'
                    helper(row, col)

        M, N = len(board), len(board[0])
        # borders row i = 0 & i = M-1
        # border cols j = 0 & j = N-1

        for i in range(M):
            for j in range(N):
                if (i in [0, M-1] or j in [0, N-1]) and board[i][j] == 'O':
                    print("inside loop")
                    board[i][j] = '#'
                    helper(i, j) 
        # print(board)
        # Now convert 0 -> X and # -> 0
        for i in range(M):
            for j in range(N):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
                
        