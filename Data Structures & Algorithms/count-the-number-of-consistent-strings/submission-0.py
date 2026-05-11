class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        _set = set(allowed)
        res = 0

        for word in words:
            for i in range(len(word)):
                if word[i] not in _set:
                    break
                
                if i == len(word)-1:
                    res += 1
        
        return res