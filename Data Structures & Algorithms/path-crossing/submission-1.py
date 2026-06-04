class Solution:
    def isPathCrossing(self, path: str) -> bool:
        N = [0, 1]
        S = [0, -1]
        E = [1, 0]
        W = [-1, 0]

        start = (0, 0)
        visit = set()
        for p in path:
            visit.add(start)
            if p == 'N':
                start = (start[0]+N[0], start[1]+N[1])
            elif p == 'S':
                start = (start[0]+S[0], start[1]+S[1])
            elif p == 'E':
                start = (start[0]+E[0], start[1]+E[1])
            elif p == 'W':
                start = (start[0]+W[0], start[1]+W[1])
            
            
            if start in visit:
                return True

        return False        