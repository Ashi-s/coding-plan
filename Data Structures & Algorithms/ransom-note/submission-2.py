class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countRansom = {}
        countMag = {}

        for r in ransomNote:
            countRansom[r] = countRansom.get(r, 0) + 1
        
        for m in magazine:
            countMag[m] = countMag.get(m, 0) + 1
        
        for key, val in countRansom.items():
            val_m = countMag.get(key, 0)

            if val_m < val:
                return False
        
        return True