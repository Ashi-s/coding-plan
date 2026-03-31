class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        d = {}

        #everyone trusts you (incoming n-1)
        # you trut no one (outgoing 0)
        incoming = defaultdict(int)
        outgoing = defaultdict(int)

        for a, b in trust:
            incoming[b] += 1
            outgoing[a] += 1
        
        for i in range(1, n+1):
            if outgoing[i] == 0 and incoming[i] == n-1:
                return i
        
        return -1