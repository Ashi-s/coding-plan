class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = {}

        for c in t:
            if c not in countT:
                countT[c] = 1
            else:
                countT[c] += 1
        
        minLen = float('inf')
        left, right = 0, 0
        for i in range(len(s)):
            countS = {}

            for j in range(i, len(s)):
                countS[s[j]] = 1 + countS.get(s[j], 0)

                flag = True
                for c in countT:
                    if countT[c] > countS.get(c, 0):
                        flag = False
                        break
                
                if flag and (j - i + 1) < minLen:
                    minLen = j - i + 1
                    left = i
                    right = j
                
        if minLen == float('inf'):
            return ""
        else:
            return s[left:right+1]
