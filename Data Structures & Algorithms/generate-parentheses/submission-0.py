class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []

        def helper(open, close):
            if len(curr) == n * 2:
                res.append(''.join(curr.copy()))
                return
            
            if open < n:
                curr.append('(')
                helper(open+1, close)
                curr.pop()
            
            if close < open:
                curr.append(')')
                helper(open, close+1)
                curr.pop()

        helper(0, 0)  
        return res
        