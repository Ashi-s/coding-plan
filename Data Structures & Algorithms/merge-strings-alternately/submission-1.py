class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        M, N = len(word1), len(word2)
        res = ""

        i, j = 0, 0

        while i < M and j < N:
            res += word1[i]
            res += word2[j]

            i += 1
            j += 1
        
        if i < M:
            res += word1[i:]
        if j < N:
            res += word2[j:]
        
        return res 
        