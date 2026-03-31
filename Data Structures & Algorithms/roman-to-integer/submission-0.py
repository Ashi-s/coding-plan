class Solution:
    def romanToInt(self, s: str) -> int:
        romanMap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        output = romanMap[s[0]]

        for i in range(1, len(s)):
            if i-1 >= 0:
                if ((s[i] == 'V' or s[i] == 'X') and s[i-1] == 'I') or ((s[i] == 'L' or s[i] == 'C') and s[i-1] == 'X') or ((s[i] == 'D' or s[i] == 'M') and s[i-1] == 'C'):
                    output -= romanMap[s[i-1]]
                    output += (romanMap[s[i]] - romanMap[s[i-1]])
                else:
                    output += romanMap[s[i]]
        return output