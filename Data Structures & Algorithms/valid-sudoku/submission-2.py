class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {} #row:set()
        cols = {} #cols:set()
        squares = {} #(r,c): set()

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                # check rows
                if r not in rows:
                    rows[r] = set()
                elif r in rows and board[r][c] in rows[r]:
                    return False
                rows[r].add(board[r][c])
                
                # check cols
                if c not in cols:
                    cols[c] = set()
                elif c in cols and board[r][c] in cols[c]:
                    return False
                cols[c].add(board[r][c])
                
                # check squares
                if (r//3, c//3) not in squares:
                    squares[(r//3, c//3)] = set()
                elif (r//3, c//3) in squares and board[r][c] in squares[(r//3, c//3)]:
                    return False
                squares[(r//3, c//3)].add(board[r][c])
        
        return True
                

