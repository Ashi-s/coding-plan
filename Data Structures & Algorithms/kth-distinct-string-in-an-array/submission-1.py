class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = {}

        for a in arr:
            count[a] = count.get(a, 0) + 1
        
        distinct = 0
        for a in arr:
            if count[a] == 1:
                distinct += 1

                if distinct == k:
                    return a
        
        return ""
        
