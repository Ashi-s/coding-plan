class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = float('-inf')
        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    res = max(res, j - i - 1)
        
        return res if res != float('-inf') else -1