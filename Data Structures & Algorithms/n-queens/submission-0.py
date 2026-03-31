class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        negD = set() # (r-c) is constant
        posD = set() # (r+c) is constant

        board = [['.']*n for _ in range(n)]
        res = []

        def helper(r):
            if r == n:
                copy = [''.join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in cols or (r+c) in posD or (r-c) in negD:
                    continue
                
                cols.add(c)
                negD.add((r-c))
                posD.add((r+c))
                board[r][c] = 'Q'
                
                helper(r+1)

                cols.remove(c)
                negD.remove((r-c))
                posD.remove((r+c))
                board[r][c] = '.'

        


        helper(0)
        return res

        