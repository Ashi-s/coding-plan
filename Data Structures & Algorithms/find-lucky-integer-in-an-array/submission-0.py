class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = {}

        for a in arr:
            d[a] = d.get(a, 0) + 1
        
        res = -1

        for key, val in d.items():
            if key == val:
                res = max(res, key)
        
        return res