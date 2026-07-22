class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiag = set()
        negDiag = set()

        board = [['.']*n for r in range(n)]

        def helper(row):
            if row == n:
                output.append([''.join(r) for r in board])
                return
            
            for c in range(n):

                if c in cols or (row+c) in posDiag or (row-c) in negDiag:
                    continue
                
                cols.add(c)
                posDiag.add((row+c))
                negDiag.add((row-c))
                board[row][c] = 'Q'
                helper(row+1)

                cols.remove(c)
                posDiag.remove((row+c))
                negDiag.remove((row-c))
                board[row][c] = '.'

        output = []
        helper(0)
        return output