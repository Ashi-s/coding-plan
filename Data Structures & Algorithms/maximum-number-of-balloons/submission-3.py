class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {}
        balloon = 'balloon'

        for t in text:
            if t in balloon:
                d[t] = d.get(t, 0) + 1
                
        #early exist if all 5 balloon characters not present
        if len(d) != 5:
            return 0
        
        res = float('inf')
        for word, count in d.items():
            if word in ['l', 'o']:
                res = min(res, count // 2)
            else:
                res = min(res, count)
        
        return 0 if res == float('inf') else res