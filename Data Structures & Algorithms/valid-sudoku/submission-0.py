class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {} # row:set()
        cols = {} # col:set()
        squares = {} # (row,col): set()


        for r in range(len(board)):
            for c in range(len(board[0])):
                val = board[r][c]
                if val == ".":
                    continue
                
                if (val in rows.get(r, set()) or 
                    val in cols.get(c, set()) or 
                    val in squares.get((r//3, c//3), set())):
                    return False
               
               
                rows.setdefault(r, set()).add(val)
                cols.setdefault(c, set()).add(val)
                squares.setdefault((r//3, c//3), set()).add(val)
        
        return True




        