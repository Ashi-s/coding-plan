class Solution:
    def maxDifference(self, s: str) -> int:
        a1 = float('-inf')
        a2 = float('inf')

        counts = {}

        for i in s:
            counts[i] = 1 + counts.get(i, 0)
        
        for key, value in counts.items():
            # even
            if value % 2 == 0:
                a2 = min(a2, value)
            # odd
            else:
                a1 = max(a1, value)
        
        return a1 - a2




